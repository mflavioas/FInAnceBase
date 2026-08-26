import os
from google.antigravity import Agent, LocalAgentConfig, types

config = LocalAgentConfig(
    vertex=True,
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
    system_instruction="""
    Você é o Planner Agent da fábrica FinKnowledge Antigravity.
    Sua missão é quebrar épicos em tarefas técnicas (User Stories, Tasks),
    gerenciar backlog e identificar dependências, alinhado ao conhecimento financeiro.
    """
)

async def run_planning(epic_description: str):
    async with Agent(config) as agent:
        response = await agent.chat(f"Gere um plano de tarefas para o épico: {epic_description}")
        return await response.text()
