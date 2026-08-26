import asyncio
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env na raiz
load_dotenv()

from google.antigravity import Agent, LocalAgentConfig, types
from agents.utils import get_base_config_kwargs

# Enable subagents in the capabilities
config = LocalAgentConfig(
    **get_base_config_kwargs(),
    capabilities=types.CapabilitiesConfig(
        enable_subagents=True,
    ),
    system_instruction="""
    Você é o Agente Orquestrador da fábrica FinKnowledge Antigravity.
    Sua missão é coordenar os agentes especializados (Planner, Architect, RAG, Trace, Regulatory, QA, Doc, Trend, Gap, Sim)
    para desenvolver o produto financeiro e analisar mercado e inovações.
    Use subagentes para delegar tarefas especializadas.
    Você deve garantir que as respostas do RAG, QA, Compliance e Análises de Inovação (Gap/Trend/Sim) 
    estejam integradas no resultado final.
    """
)

async def main():
    if not os.getenv("GEMINI_API_KEY"):
        print("Aviso: GEMINI_API_KEY não encontrada. As requisições falharão sem uma chave de API válida.")
    
    print("Iniciando Orquestrador FinKnowledge Antigravity...")
    async with Agent(config) as agent:
        # Exemplo de comando que delega para subagentes
        epic_prompt = "Crie uma análise inicial de arquitetura para o produto de Crédito Consignado INSS usando o Architect Agent e depois planeje as tarefas usando o Planner Agent."
        print(f"Enviando épico para orquestração: {epic_prompt}")
        
        try:
            response = await agent.chat(epic_prompt)
            print("\n=== Resultado da Orquestração ===\n")
            print(await response.text())
        except types.AntigravityConnectionError as e:
            print(f"\n[ERRO DE CONEXÃO] Falha de comunicação com a API: {e}")
            print("Verifique sua conexão com a internet ou sua GEMINI_API_KEY.")
        except types.AntigravityValidationError as e:
            print(f"\n[ERRO DE VALIDAÇÃO] Parâmetros inválidos fornecidos: {e}")

if __name__ == "__main__":
    asyncio.run(main())
