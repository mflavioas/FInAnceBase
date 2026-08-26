import os
from google.antigravity import Agent, LocalAgentConfig, types
from agents.utils import get_base_config_kwargs

config = LocalAgentConfig(
    **get_base_config_kwargs(),
    system_instruction="""
    Você é o Agente Avaliador de IA (AI Eval) da fábrica FinKnowledge Antigravity.
    Sua missão é testar a qualidade das respostas geradas por outros agentes do sistema.
    Você deve avaliar métricas como: coesão, falta de alucinação (groundedness) e alinhamento
    com os regulamentos financeiros.
    """
)

async def evaluate_ai_response(agent_name: str, prompt: str, ai_response: str):
    async with Agent(config) as agent:
        eval_prompt = f"""
        Avalie a seguinte resposta gerada pelo agente '{agent_name}'.
        
        [Prompt Original]: {prompt}
        [Resposta da IA]: {ai_response}
        
        Gere uma avaliação contendo:
        1. Score Geral (0-100)
        2. Métricas: Toxicidade (0-10), Coesão (0-10), Embasamento/Groundedness (0-10).
        3. Feedback textual apontando melhorias.
        """
        response = await agent.chat(eval_prompt)
        return await response.text()
