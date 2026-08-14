from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="FinKnowledge Antigravity API",
    description="API para Plataforma de Conhecimento Financeiro Auto-documentada com IA",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    # Placeholder for Prometheus metrics
    return {"status": "ok", "metrics": {}}

from apps.api.routers import sources, documents, taxonomy, architecture, search, graph, inventory

app.include_router(sources.router)
app.include_router(documents.router)
app.include_router(taxonomy.router)
app.include_router(architecture.router)
app.include_router(search.router)
app.include_router(graph.router)
app.include_router(inventory.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
