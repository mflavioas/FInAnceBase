from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from db.models import SourceType, SourceStatus
# In a real app we would use SQLAlchemy Session, but here we mock for simplicity of Fase 1 API scaffold

router = APIRouter(prefix="/sources", tags=["Sources"])

class SourceCreate(BaseModel):
    name: str
    url: str
    source_type: SourceType
    entity: Optional[str] = None

class SourceResponse(SourceCreate):
    id: str
    status: SourceStatus

@router.post("/", response_model=SourceResponse)
def create_source(source: SourceCreate):
    # Mock return
    return SourceResponse(
        id="mock-uuid-1234",
        name=source.name,
        url=source.url,
        source_type=source.source_type,
        entity=source.entity,
        status=SourceStatus.ACTIVE
    )

@router.get("/", response_model=List[SourceResponse])
def list_sources():
    # Mock return
    return []

@router.post("/{source_id}/trigger")
def trigger_collection(source_id: str):
    # This endpoint would send a Celery task to collect documents
    return {"message": "Collection triggered in background."}
