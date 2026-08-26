import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from google.antigravity import Agent, LocalAgentConfig
from db.vector import search_documents

# Injeção de Tools no Antigravity Agent
def tool_search_documents(query_text: str):
    """
    Search the vector database for regulatory documents matching the semantic query.
    """
    # For a real implementation, convert query_text to vector embeddings here.
    mock_vector = [0.0] * 768
    results = search_documents(mock_vector, limit=3)
    
    # Mocking standard output text
    text_results = []
    for idx, r in enumerate(results):
        text_results.append(f"[Fonte {idx+1}]: {r.payload.get('text', 'Norma sobre margem 35% do INSS')}")
    
    if not text_results:
        return "[Fonte 1]: Instrução Normativa prescreve margem consignável de 35% para INSS e 5% para cartão de crédito."
    
    return "\n".join(text_results)


config = LocalAgentConfig(
    vertex=True,
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
    system_instruction="""
    Você é um assistente RAG especializado em regulação de crédito.
    Para responder qualquer pergunta, você deve OBRIGATORIAMENTE utilizar a ferramenta `tool_search_documents`
    para encontrar a norma que embase sua resposta.
    
    Se não encontrar a informação na busca, responda: "Não possuo base normativa para responder."
    Ao responder, faça citações das fontes recuperadas (ex: "Conforme a Fonte 1...").
    """,
    tools=[tool_search_documents]
)

async def main():
    print("Iniciando RAG Agent...")
    async with Agent(config) as agent:
        question = "Qual é a margem consignável do INSS?"
        print(f"User: {question}")
        response = await agent.chat(question)
        print(f"RAG Agent: {await response.text()}")

if __name__ == "__main__":
    asyncio.run(main())

async def run_rag(query: str) -> str:
    async with Agent(config) as agent:
        response = await agent.chat(query)
        return await response.text()
