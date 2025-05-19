import os
import glob
import frontmatter
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
from typing import List, Dict, Optional
from pathlib import Path
import markdown
from bs4 import BeautifulSoup

class DocumentIndexer:
    def __init__(self, docs_dir: str = "../docs"):
        """Initialize the document indexer with ChromaDB"""
        self.docs_dir = Path(docs_dir)
        self.chroma_client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory="./chroma_db"
        ))
        
        # Using all-MiniLM-L6-v2 model for embeddings (small but effective)
        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        
        # Create or get the collection
        self.collection = self.chroma_client.get_or_create_collection(
            name="o3_docs",
            embedding_function=self.embedding_function
        )
    
    def extract_text_from_markdown(self, file_path: Path) -> str:
        """Extract clean text from markdown file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse frontmatter if exists
        try:
            post = frontmatter.loads(content)
            content = post.content
        except:
            pass
            
        # Convert markdown to HTML then to plain text
        html = markdown.markdown(content)
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text(separator='\n', strip=True)
    
    def chunk_text(self, text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
        """Split text into overlapping chunks"""
        words = text.split()
        chunks = []
        
        for i in range(0, len(words), chunk_size - overlap):
            chunk = ' '.join(words[i:i + chunk_size])
            chunks.append(chunk)
            
        return chunks
    
    def index_documents(self):
        """Index all markdown files in the docs directory"""
        # Get all markdown files
        md_files = list(self.docs_dir.rglob('**/*.md'))
        
        print(f"Found {len(md_files)} markdown files to index...")
        
        for file_path in md_files:
            try:
                # Skip if file is in .git directory
                if '.git' in str(file_path):
                    continue
                    
                print(f"Indexing: {file_path.relative_to(self.docs_dir)}")
                
                # Extract and clean text
                text = self.extract_text_from_markdown(file_path)
                
                # Skip if empty
                if not text.strip():
                    continue
                
                # Chunk the document
                chunks = self.chunk_text(text)
                
                # Prepare documents for indexing
                doc_id = str(file_path.relative_to(self.docs_dir))
                documents = []
                metadatas = []
                ids = []
                
                for i, chunk in enumerate(chunks):
                    chunk_id = f"{doc_id}__chunk_{i}"
                    metadata = {
                        "source": str(file_path.relative_to(self.docs_dir)),
                        "chunk": i,
                        "total_chunks": len(chunks)
                    }
                    
                    documents.append(chunk)
                    metadatas.append(metadata)
                    ids.append(chunk_id)
                
                # Add to Chroma
                if documents:
                    self.collection.add(
                        documents=documents,
                        metadatas=metadatas,
                        ids=ids
                    )
                
                print(f"  → Added {len(chunks)} chunks")
                
            except Exception as e:
                print(f"Error processing {file_path}: {str(e)}")
                continue
        
        # Persist the database
        self.chroma_client.persist()
        print("\nIndexing complete!")

class DocumentRetriever:
    def __init__(self):
        """Initialize the document retriever"""
        self.chroma_client = chromadb.PersistentClient(path="./chroma_db")
        
        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        
        self.collection = self.chroma_client.get_collection(
            name="o3_docs",
            embedding_function=self.embedding_function
        )
    
    def query(self, query_text: str, n_results: int = 5) -> List[Dict]:
        """Query the document collection"""
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        
        # Format results
        formatted_results = []
        for i in range(len(results['documents'][0])):
            formatted_results.append({
                'document': results['documents'][0][i],
                'metadata': results['metadatas'][0][i],
                'distance': results['distances'][0][i]
            })
            
        return formatted_results

if __name__ == "__main__":
    # Create the vector database and index documents
    print("Creating document index...")
    indexer = DocumentIndexer()
    indexer.index_documents()
    
    # Example query
    print("\nTesting document retrieval...")
    retriever = DocumentRetriever()
    query = "How do I implement growth loops?"
    print(f"Query: {query}")
    
    results = retriever.query(query)
    
    print("\nTop results:")
    for i, result in enumerate(results, 1):
        print(f"\n--- Result {i} (distance: {result['distance']:.4f}) ---")
        print(f"Source: {result['metadata']['source']}")
        print(f"Chunk {result['metadata']['chunk'] + 1} of {result['metadata']['total_chunks']}")
        print("-" * 50)
        print(result['document'][:300] + "..." if len(result['document']) > 300 else result['document'])
