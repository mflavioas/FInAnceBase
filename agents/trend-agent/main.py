from google.antigravity import Agent, LocalAgentConfig, types

config = LocalAgentConfig(
    system_instruction="""
    Você é o Trend Agent (Head de Inovação) da fábrica FinKnowledge Antigravity.
    Sua missão é avaliar feeds de notícias ou mudanças regulatórias e classificá-las em:
    produto, tecnologia, regulação, experiência ou risco.
    Você também deve gerar um score de relevância (0 a 100) para cada tendência identificada
    e sugerir quais domínios do sistema serão mais afetados.
    """
)

async def run_trend_analysis(news_content: str):
    async with Agent(config) as agent:
        prompt = f"""
        Analise a seguinte fonte externa de inovação ou regulação e extraia:
        1. Categoria(s) (produto, tecnologia, regulação, experiência, risco).
        2. Score de relevância (0-100).
        3. Domínios afetados.
        4. Resumo da oportunidade.

        Conteúdo:
        {news_content}
        """
        response = await agent.chat(prompt)
        return await response.text()
