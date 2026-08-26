import os
from google.antigravity import Agent, LocalAgentConfig, types

config = LocalAgentConfig(
    vertex=True,
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
    system_instruction="""
    Você é o Agente QA (Quality Assurance) da fábrica FinKnowledge Antigravity.
    Sua missão é gerar cenários de teste (funcionais e não funcionais) a partir de regras de negócio,
    épicos, histórias de usuário ou normativos.
    Você deve vincular cenários às regras/capacidades, sugerir testes automatizados
    e gerar exemplos de massa de dados.
    """
)

async def run_qa_generation(requirements: str):
    async with Agent(config) as agent:
        prompt = f"""
        Com base nos seguintes requisitos/regras, por favor gere:
        1. Cenários de teste funcionais e não funcionais.
        2. Vínculo dos cenários com as regras e capacidades.
        3. Sugestão de abordagem para testes automatizados.
        4. Exemplos de massa de dados para os testes.

        Requisitos:
        {requirements}
        """
        response = await agent.chat(prompt)
        return await response.text()
