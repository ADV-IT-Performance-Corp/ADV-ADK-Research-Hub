# O3 Deep Research - Vector Database

This directory contains the vector database implementation for the O3 Deep Research system, enabling semantic search across all documentation.

## Features

- **Document Indexing**: Automatically indexes all markdown files in the `docs` directory
- **Semantic Search**: Find relevant information using natural language queries
- **REST API**: Simple HTTP API for integration with other services
- **Chunking**: Intelligent document chunking with overlap for better context

## Setup

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the indexer to create the vector database:
   ```bash
   python vector_indexer.py
   ```
   This will process all markdown files in the `../docs` directory and create a `chroma_db` folder with the vector embeddings.

## Usage

### Command Line

After indexing, you can run the API server:

```bash
python api.py
```

The API will be available at `http://localhost:8000`

### API Endpoints

- `GET /health` - Check if the service is running
- `POST /query` - Query the document collection

#### Example Query

```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"query": "How do I implement growth loops?", "n_results": 3}'
```

### Integration with O3 Deep Research

You can use the vector database to enhance the O3 Deep Research prompt with relevant context:

```python
import requests

def get_relevant_context(query: str, n_results: int = 3) -> str:
    """Get relevant context from the vector database"""
    try:
        response = requests.post(
            "http://localhost:8000/query",
            json={"query": query, "n_results": n_results}
        )
        response.raise_for_status()
        results = response.json()
        
        context = "## Relevant Context from Knowledge Base\n\n"
        for i, result in enumerate(results, 1):
            context += f"### Source: {result['metadata']['source']} (Score: {result['score']:.2f})\n"
            context += f"{result['document']}\n\n"
            
        return context
    except Exception as e:
        print(f"Error querying vector database: {e}")
        return ""

# Example usage in your O3 Deep Research prompt
query = "How should I structure my marketing automation system?"
context = get_relevant_context(query)

prompt = f"""You are O3 Deep Research - an AI research assistant.

{context}

Question: {query}"""
```

## Performance

- **Indexing**: ~1-2 seconds per document (depends on document size)
- **Query Latency**: ~100-300ms on CPU
- **Storage**: ~100MB per 1,000 pages of text

## Customization

### Changing the Embedding Model

Edit the `vector_indexer.py` file to use a different model:

```python
# In DocumentIndexer.__init__
self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-mpnet-base-v2"  # Larger model, better quality
)
```

### Adjusting Chunking

Modify the `chunk_text` method in `vector_indexer.py`:

```python
def chunk_text(self, text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
    # Your custom chunking logic here
    pass
```

## License

MIT
