from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import importlib

sim_module = importlib.import_module("agents.sim-agent.main")
run_product_simulation = sim_module.run_product_simulation

router = APIRouter(prefix="/simulator", tags=["Simulador de Novo Produto"])

class SimulationRequest(BaseModel):
    product_params: str

class SimulationResponse(BaseModel):
    simulation_result: str

@router.post("/run", response_model=SimulationResponse)
async def run_simulation(req: SimulationRequest):
    try:
        # User explicitly requested synchronous API for MVP
        result = await run_product_simulation(req.product_params)
        return SimulationResponse(simulation_result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
