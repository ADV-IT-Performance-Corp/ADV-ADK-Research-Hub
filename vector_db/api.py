from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
from vector_indexer import DocumentRetriever
import uvicorn

app = FastAPI(
    title="O3 Deep Research API",
    description="API for querying the O3 Deep Research knowledge base",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the retriever
retriever = None

try:
    retriever = DocumentRetriever()
    print("Document retriever initialized successfully!")
except Exception as e:
    print(f"Error initializing document retriever: {str(e)}")

class QueryRequest(BaseModel):
    query: str
    n_results: int = 5

class SearchResult(BaseModel):
    document: str
    metadata: dict
    score: float

@app.on_event("startup")
async def startup_event():
    global retriever
    try:
        retriever = DocumentRetriever()
    except Exception as e:
        print(f"Error initializing document retriever: {str(e)}")
        raise

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    if not retriever:
        raise HTTPException(status_code=503, detail="Document retriever not initialized")
    return {"status": "ok"}

@app.post("/query", response_model=List[SearchResult])
async def query_documents(request: QueryRequest):
    """
    Query the document collection
    """
    if not retriever:
        raise HTTPException(status_code=503, detail="Document retriever not initialized")
    
    try:
        results = retriever.query(request.query, request.n_results)
        # Convert distance to similarity score (1 / (1 + distance))
        formatted_results = []
        for result in results:
            formatted_results.append({
                "document": result["document"],
                "metadata": result["metadata"],
                "score": 1.0 / (1.0 + result["distance"])
            })
        return formatted_results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
