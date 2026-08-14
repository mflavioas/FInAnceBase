from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/inventory", tags=["Systems Inventory"])

class ServiceCreate(BaseModel):
    name: str
    domain: str
    repository_id: Optional[str] = None
    description: Optional[str] = None

class ServiceResponse(ServiceCreate):
    id: str
    status: str

@router.post("/services", response_model=ServiceResponse)
def create_service(service: ServiceCreate):
    return ServiceResponse(
        id="uuid-svc-01",
        status="ACTIVE",
        **service.model_dump()
    )

@router.get("/services", response_model=List[ServiceResponse])
def list_services():
    return []

class APIEndpointCreate(BaseModel):
    service_id: str
    method: str
    path: str
    description: Optional[str] = None

class APIEndpointResponse(APIEndpointCreate):
    id: str

@router.post("/endpoints", response_model=APIEndpointResponse)
def create_endpoint(endpoint: APIEndpointCreate):
    return APIEndpointResponse(
        id="uuid-ep-01",
        **endpoint.model_dump()
    )
