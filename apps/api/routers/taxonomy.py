from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/taxonomy", tags=["Taxonomy & Catalogs"])

class ProductCreate(BaseModel):
    code: str
    name: str
    family: str
    segment: str
    description: Optional[str] = None

class ProductResponse(ProductCreate):
    id: str
    status: str

@router.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate):
    # Mocking DB insertion
    return ProductResponse(
        id="uuid-prod-01",
        status="ACTIVE",
        **product.model_dump()
    )

@router.get("/products", response_model=List[ProductResponse])
def list_products():
    return []

class AgreementCreate(BaseModel):
    code: str
    name: str
    agreement_type: str
    integration_channel: Optional[str] = None
    specific_rules: Optional[dict] = None

class AgreementResponse(AgreementCreate):
    id: str
    status: str

@router.post("/agreements", response_model=AgreementResponse)
def create_agreement(agreement: AgreementCreate):
    return AgreementResponse(
        id="uuid-agr-01",
        status="ACTIVE",
        **agreement.model_dump()
    )
