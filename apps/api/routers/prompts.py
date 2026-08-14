from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional, Dict
from db.models import PromptRegistry, StatusEnum
from sqlalchemy.orm import Session

# Since I don't know the exact dependency for Session, I will mock it temporarily or look it up.
# For now I will build the router structure.

router = APIRouter(prefix="/prompts", tags=["Prompt Registry"])

class PromptCreate(BaseModel):
    name: str
    version: str
    objective: Optional[str] = None
    model_name: str
    system_prompt: str
    parameters: Optional[Dict] = None
    owner: Optional[str] = None

class PromptResponse(PromptCreate):
    id: str
    status: StatusEnum

@router.post("/", response_model=PromptResponse)
def create_prompt(prompt: PromptCreate):
    # Mock implementation until DB dependency is injected
    return PromptResponse(
        id="mock-id",
        name=prompt.name,
        version=prompt.version,
        objective=prompt.objective,
        model_name=prompt.model_name,
        system_prompt=prompt.system_prompt,
        parameters=prompt.parameters,
        owner=prompt.owner,
        status=StatusEnum.ACTIVE
    )

@router.get("/{prompt_id}", response_model=PromptResponse)
def get_prompt(prompt_id: str):
    # Mock implementation
    return PromptResponse(
        id=prompt_id,
        name="Mock Prompt",
        version="v1.0",
        objective="Do something",
        model_name="gemini-1.5-pro",
        system_prompt="You are a helpful AI",
        parameters={"temperature": 0.2},
        owner="admin",
        status=StatusEnum.ACTIVE
    )
