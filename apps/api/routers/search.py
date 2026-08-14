from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from db.vector import search_documents

router = APIRouter(prefix="/search", tags=["Semantic Search & RAG"])

class SearchQuery(BaseModel):
    query: str
    limit: Optional[int] = 5
    product_id: Optional[str] = None
    entity: Optional[str] = None

class SearchResult(BaseModel):
    document_id: str
    text_snippet: str
    score: float
    metadata: dict

@router.post("/", response_model=List[SearchResult])
def semantic_search(search: SearchQuery):
    # In a real scenario we'd use an embedding model to convert query to vector
    mock_vector = [0.0] * 768
    
    # Executa busca no Qdrant
    results = search_documents(mock_vector, limit=search.limit)
    
    # Mock return until embedding is fully integrated
    return [
        SearchResult(
            document_id="doc-123",
            text_snippet="A margem consignável aplicável aos benefícios do INSS é de 35%.",
            score=0.98,
            metadata={"product": "Crédito Consignado", "source": "Instrução Normativa INSS"}
        )
    ]
