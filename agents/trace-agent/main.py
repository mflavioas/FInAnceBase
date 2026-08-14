import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from google.antigravity import Agent, LocalAgentConfig
from db.graph import graph_db

def tool_trace_openapi(openapi_json_content: str):
    """
    Simulates parsing an OpenAPI document and correlating to business capabilities in the graph.
    """
    print(f"Parsing OpenAPI with size: {len(openapi_json_content)} bytes")
    # Em um cenário real, aqui criaríamos nós e relacionamentos no Neo4j (Service -> API -> Capability)
    cypher = """
    MERGE (s:Service {name: 'CreditCardAPI'})
    MERGE (ep:APIEndpoint {path: '/api/v1/credit'})
    MERGE (c:Capability {name: 'Reserva de Margem'})
    MERGE (s)-[:EXPOSES]->(ep)
    MERGE (ep)-[:IMPLEMENTS]->(c)
    RETURN s, ep, c
    """
    results = graph_db.run_query(cypher)
    return "APIs mapeadas com sucesso para a Capacidade 'Reserva de Margem'."


config = LocalAgentConfig(
    system_instruction="""
    Você é um agente de rastreabilidade especializado em arquitetura de software e governança corporativa.
    Seu papel é ler especificações OpenAPI ou definições de repositórios e extrair o inventário.
    Você OBRIGATORIAMENTE deve usar a ferramenta `tool_trace_openapi` para indexar a especificação no Grafo de Conhecimento.
    """,
    tools=[tool_trace_openapi]
)

async def main():
    print("Iniciando Trace Agent...")
    async with Agent(config) as agent:
        openapi_mock = '{"openapi": "3.0.0", "info": {"title": "CreditCardAPI"}, "paths": {"/api/v1/credit": {}}}'
        print(f"User: Analise o arquivo OpenAPI e extraia os inventários: {openapi_mock}")
        response = await agent.chat(f"Analise e extraia: {openapi_mock}")
        print(f"Trace Agent: {await response.text()}")

if __name__ == "__main__":
    asyncio.run(main())
