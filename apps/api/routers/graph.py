from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from db.graph import graph_db

router = APIRouter(prefix="/graph", tags=["Knowledge Graph"])

class ImpactQuery(BaseModel):
    entity_id: str
    entity_type: str # e.g. "Rule", "Regulation", "Service"

@router.post("/impact", response_model=List[dict])
def query_impact(query: ImpactQuery):
    # Example cypher query to find affected capabilities
    cypher = """
    MATCH (r:Rule {id: $entity_id})-[:AFFECTS]->(c:Capability)
    RETURN c.name AS capability, c.domain AS domain
    """
    results = graph_db.run_query(cypher, {"entity_id": query.entity_id})
    
    if not results:
        # Mock for PoC if Neo4j is empty
        return [
            {"capability": "Reserva de Margem", "domain": "Crédito"},
            {"capability": "Simulação", "domain": "Crédito"}
        ]
    return results
