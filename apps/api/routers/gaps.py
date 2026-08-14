from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import importlib

gap_module = importlib.import_module("agents.gap-agent.main")
run_gap_analysis = gap_module.run_gap_analysis

router = APIRouter(prefix="/gaps", tags=["Análise de Gaps"])

class GapAnalysisRequest(BaseModel):
    product_id: str
    required_capabilities: str
    current_capabilities: str

class GapAnalysisResponse(BaseModel):
    analysis_result: str

@router.post("/analyze", response_model=GapAnalysisResponse)
async def analyze_gap(req: GapAnalysisRequest):
    try:
        result = await run_gap_analysis(req.required_capabilities, req.current_capabilities)
        return GapAnalysisResponse(analysis_result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
