from google.antigravity import Agent, LocalAgentConfig, types

config = LocalAgentConfig(
    system_instruction="""
    Você é o Gap Agent (Product Manager focado em Lacunas) da fábrica FinKnowledge Antigravity.
    Sua missão é receber as capacidades ideais de um produto e compará-las com as capacidades 
    implementadas atualmente. Você deve identificar e categorizar os "gaps" (lacunas) em:
    funcionais, técnicas, regulatórias, testes ou integração.
    Você também deve sugerir épicos para fechar esses gaps.
    """
)

async def run_gap_analysis(required_capabilities: str, current_capabilities: str):
    async with Agent(config) as agent:
        prompt = f"""
        Realize uma análise de Gap com base nas informações abaixo:
        
        [Capacidades Necessárias]:
        {required_capabilities}
        
        [Capacidades Atuais do Sistema]:
        {current_capabilities}
        
        Por favor, gere:
        1. Lista de lacunas categorizadas.
        2. Score de prioridade baseado em risco e valor (ex: Alta, Média, Baixa).
        3. Sugestão de Épicos para desenvolvimento.
        """
        response = await agent.chat(prompt)
        return await response.text()
