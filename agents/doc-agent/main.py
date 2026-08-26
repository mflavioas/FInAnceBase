import os
from google.antigravity import Agent, LocalAgentConfig, types

config = LocalAgentConfig(
    vertex=True,
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
    system_instruction="""
    Você é o Agente de Documentação Automática (Tech Lead AI) da fábrica FinKnowledge Antigravity.
    Sua missão é gerar ou atualizar documentações técnicas (README, ADRs, dicionário de dados, 
    API docs, runbooks, changelog) com base em mudanças de código, schema ou prompts detectadas.
    Você deve ser preciso e direto, atualizando a documentação para que reflita a realidade atual do sistema.
    """
)

async def run_doc_generation(changes: str, doc_type: str = "Geral"):
    async with Agent(config) as agent:
        prompt = f"""
        Com base nas seguintes mudanças no projeto:
        {changes}
        
        Por favor, gere/atualize o documento do tipo: {doc_type}.
        Se for necessário, estruture a saída no formato Markdown padrão, pronto para ser consolidado
        em um Pull Request de documentação.
        """
        response = await agent.chat(prompt)
        return await response.text()
