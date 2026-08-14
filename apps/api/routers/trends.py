from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import importlib

trend_module = importlib.import_module("agents.trend-agent.main")
run_trend_analysis = trend_module.run_trend_analysis

router = APIRouter(prefix="/trends", tags=["Radar de Tendências"])

class TrendAnalyzeRequest(BaseModel):
    news_content: str

class TrendResponse(BaseModel):
    analysis_result: str

@router.post("/analyze", response_model=TrendResponse)
async def analyze_trend(req: TrendAnalyzeRequest):
    try:
        result = await run_trend_analysis(req.news_content)
        return TrendResponse(analysis_result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
