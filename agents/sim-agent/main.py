import os
from google.antigravity import Agent, LocalAgentConfig, types

config = LocalAgentConfig(
    vertex=True,
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
    system_instruction="""
    Você é o Simulator Agent (Arquiteto de Produtos) da fábrica FinKnowledge Antigravity.
    Sua missão é receber parâmetros básicos de um novo produto (família, modalidade, desconto, canal, garantias)
    e realizar uma simulação para estimar o esforço de criação.
    Você deve indicar as capacidades necessárias, normas prováveis aplicáveis e sugerir reusos
    de capacidades existentes do sistema.
    """
)

async def run_product_simulation(product_params: str):
    async with Agent(config) as agent:
        prompt = f"""
        Realize a simulação de criação para o novo produto financeiro com os seguintes parâmetros:
        
        {product_params}
        
        Por favor, gere um documento de viabilidade inicial contendo:
        1. Capacidades Necessárias.
        2. Contextos (Bounded Contexts).
        3. Normas prováveis.
        4. Integrações necessárias.
        5. Sugestões de reuso de domínios ou serviços existentes.
        6. Riscos associados.
        """
        response = await agent.chat(prompt)
        return await response.text()
