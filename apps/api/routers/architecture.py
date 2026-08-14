from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/architecture", tags=["Enterprise Architecture"])

class BoundedContextCreate(BaseModel):
    name: str
    domain: str
    description: Optional[str] = None

class BoundedContextResponse(BoundedContextCreate):
    id: str

@router.post("/bounded-contexts", response_model=BoundedContextResponse)
def create_bounded_context(ctx: BoundedContextCreate):
    return BoundedContextResponse(
        id="uuid-bc-01",
        **ctx.model_dump()
    )

@router.get("/bounded-contexts", response_model=List[BoundedContextResponse])
def list_bounded_contexts():
    return []

class CapabilityCreate(BaseModel):
    name: str
    domain: str
    description: Optional[str] = None
    parent_id: Optional[str] = None

class CapabilityResponse(CapabilityCreate):
    id: str

@router.post("/capabilities", response_model=CapabilityResponse)
def create_capability(cap: CapabilityCreate):
    return CapabilityResponse(
        id="uuid-cap-01",
        **cap.model_dump()
    )
