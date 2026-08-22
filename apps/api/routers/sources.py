from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Form
from pydantic import BaseModel
from typing import List, Optional
from db.models import SourceType, SourceStatus, Source
from sqlalchemy.orm import Session
from db.session import get_db
import os
import shutil
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
def create_source(source: SourceCreate, db: Session = Depends(get_db)):
    db_source = Source(
        name=source.name,
        url=source.url,
        source_type=source.source_type,
        entity=source.entity,
        status=SourceStatus.ACTIVE
    )
    db.add(db_source)
    db.commit()
    db.refresh(db_source)
    return db_source

@router.get("/", response_model=List[SourceResponse])
def list_sources(db: Session = Depends(get_db)):
    sources = db.query(Source).all()
    return sources

@router.post("/{source_id}/trigger")
def trigger_collection(source_id: str):
    # This endpoint would send a Celery task to collect documents
    return {"message": "Collection triggered in background."}

UPLOAD_DIR = "apps/api/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload", response_model=SourceResponse)
async def upload_source(
    file: UploadFile = File(...),
    name: str = Form(...),
    entity: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    db_source = Source(
        name=name,
        url=file_path,
        source_type=SourceType.INTERNAL,
        entity=entity,
        status=SourceStatus.ACTIVE
    )
    db.add(db_source)
    db.commit()
    db.refresh(db_source)
    
    return db_source
