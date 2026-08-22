from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="FinKnowledge Antigravity API",
    description="API para Plataforma de Conhecimento Financeiro Auto-documentada com IA",
    version="1.0.0"
)

from fastapi.responses import RedirectResponse

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    # Placeholder for Prometheus metrics
    return {"status": "ok", "metrics": {}}

from apps.api.routers import sources, documents, taxonomy, architecture, search, graph, inventory, assistant, prompts, trends, gaps, simulator, auth, governance

app.include_router(auth.router)
app.include_router(sources.router)
app.include_router(documents.router)
app.include_router(taxonomy.router)
app.include_router(architecture.router)
app.include_router(search.router)
app.include_router(graph.router)
app.include_router(inventory.router)
app.include_router(assistant.router)
app.include_router(prompts.router)
app.include_router(trends.router)
app.include_router(gaps.router)
app.include_router(simulator.router)
app.include_router(governance.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
