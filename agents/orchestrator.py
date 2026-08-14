import asyncio
import os
from google.antigravity import Agent, LocalAgentConfig, types

# Enable subagents in the capabilities
config = LocalAgentConfig(
    capabilities=types.CapabilitiesConfig(
        enable_subagents=True,
    ),
    system_instruction="""
    Você é o Agente Orquestrador da fábrica FinKnowledge Antigravity.
    Sua missão é coordenar os agentes especializados (Planner, Architect, RAG, Trace, Regulatory, QA, Doc)
    para desenvolver o produto financeiro. Use subagentes para delegar tarefas especializadas.
    Você deve garantir que as respostas do RAG, QA e Compliance estão integradas no resultado final.
    """
)

async def main():
    if not os.getenv("GEMINI_API_KEY"):
        print("Aviso: GEMINI_API_KEY não encontrada. As respostas podem falhar se a autenticação não estiver configurada no ambiente.")
    
    print("Iniciando Orquestrador FinKnowledge Antigravity...")
    async with Agent(config) as agent:
        # Exemplo de comando que delega para subagentes
        epic_prompt = "Crie uma análise inicial de arquitetura para o produto de Crédito Consignado INSS usando o Architect Agent e depois planeje as tarefas usando o Planner Agent."
        print(f"Enviando épico para orquestração: {epic_prompt}")
        
        response = await agent.chat(epic_prompt)
        print("\n=== Resultado da Orquestração ===\n")
        print(await response.text())

if __name__ == "__main__":
    asyncio.run(main())
