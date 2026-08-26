import os
from google.antigravity import Agent, LocalAgentConfig, types

config = LocalAgentConfig(
    vertex=True,
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
    system_instruction="""
    Você é o Architect Agent da fábrica FinKnowledge Antigravity.
    Sua missão é sugerir bounded contexts, serviços, eventos, integrações e APIs
    para os épicos fornecidos pelo Planner. Use a base de conhecimento do PRD.
    """
)

async def run_architect_analysis(context: str):
    async with Agent(config) as agent:
        response = await agent.chat(f"Analise a arquitetura para o seguinte contexto: {context}")
        return await response.text()
