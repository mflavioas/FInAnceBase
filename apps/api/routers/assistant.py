from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import importlib

rag_module = importlib.import_module("agents.rag-agent.main")
run_rag = rag_module.run_rag

router = APIRouter(prefix="/assistant", tags=["Conversational Assistant"])

class ChatRequest(BaseModel):
    query: str
    session_id: Optional[str] = None
    product_id: Optional[str] = None
    entity: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    session_id: Optional[str] = None

@router.post("/chat", response_model=ChatResponse)
async def chat_with_assistant(chat_req: ChatRequest):
    try:
        # Pass the query to the RAG Agent.
        # Ideally, session_id should be used to retrieve conversation history from DB.
        context_prefix = ""
        if chat_req.product_id:
            context_prefix += f"[Contexto Produto: {chat_req.product_id}] "
        if chat_req.entity:
            context_prefix += f"[Contexto Entidade: {chat_req.entity}] "
            
        full_query = context_prefix + chat_req.query
        response_text = await run_rag(full_query)
        
        return ChatResponse(
            response=response_text,
            session_id=chat_req.session_id or "new_session"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
