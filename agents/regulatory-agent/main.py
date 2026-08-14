from google.antigravity import Agent, LocalAgentConfig, types

config = LocalAgentConfig(
    system_instruction="""
    Você é o Agente Regulatório (Compliance) da fábrica FinKnowledge Antigravity.
    Sua missão é analisar mudanças normativas, comparar versões de normas, extrair obrigações
    e identificar impactos nos produtos e serviços catalogados.
    Para itens incertos ou de alto risco, você deve marcá-los para validação humana.
    """
)

async def run_regulatory_analysis(old_norm: str, new_norm: str, context: str = ""):
    async with Agent(config) as agent:
        prompt = f"""
        Analise a seguinte mudança normativa:
        Contexto/Produtos: {context}
        
        [Versão Anterior]:
        {old_norm}
        
        [Nova Versão]:
        {new_norm}
        
        Por favor, gere um relatório contendo:
        1. Comparativo das principais mudanças.
        2. Extração das obrigações.
        3. Relação de impacto nos produtos/serviços.
        4. Itens que exigem validação humana.
        """
        response = await agent.chat(prompt)
        return await response.text()
