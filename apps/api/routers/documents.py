from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from db.models import DocumentStatus

router = APIRouter(prefix="/documents", tags=["Documents"])

class DocumentReview(BaseModel):
    approved: bool
    review_notes: str = ""

@router.get("/pending-review", response_model=List[dict])
def list_pending_review():
    # Mock
    return []

@router.post("/{doc_id}/review")
def review_document(doc_id: str, review: DocumentReview):
    status = DocumentStatus.APPROVED if review.approved else DocumentStatus.REJECTED
    # Enqueue a celery task for indexing if approved
    return {"message": f"Document {doc_id} marked as {status.value}"}
