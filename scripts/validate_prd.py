import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from google.antigravity import Agent, LocalAgentConfig

config = LocalAgentConfig(
    system_instruction="""
    Você é um Agente Auditor focado em validar as entregas do projeto contra o PRD (Product Requirements Document).
    Sua missão é ler o conteúdo do PRD e compará-lo com o código e arquitetura existentes.
    Gere um relatório detalhado do que foi concluído, o que está pendente, e eventuais desvios.
    """
)

async def main():
    try:
        with open("docs/prd.md", "r", encoding="utf-8") as f:
            prd_content = f.read()
            
        print("Iniciando Agente de Validação contra o PRD...")
        
        # Em um cenário real, você extrairia a árvore de diretórios ou metadados de arquivos
        # Aqui, vamos passar um resumo da estrutura do projeto como contexto.
        project_structure = """
        - apps/api/main.py (FastAPI com rotas)
        - apps/api/routers/ (assistant, architecture, documents, graph, inventory, search, sources, taxonomy, prompts)
        - agents/ (architect-agent, pm-agent, rag-agent, trace-agent, regulatory-agent, qa-agent, doc-agent, orchestrator.py)
        - db/models.py (Tabelas SQLAlchemy para Fases 1, 2, 4 e 5)
        - db/migrations/ (Alembic files up to fase5_prompts)
        """

        async with Agent(config) as agent:
            prompt = f"""
            PRD:\n{prd_content[:4000]}... [Conteúdo Truncado para a análise da Fase 5]\n\n
            Estrutura Atual do Projeto:\n{project_structure}\n\n
            Analise se as User Stories da Fase 5 (Assistente, Arquiteto, PM, Regulatório, QA, Doc, Prompt Registry)
            foram estruturalmente implementadas.
            """
            
            response = await agent.chat(prompt)
            report = await response.text()
            
            with open("docs/reports/validation_report.md", "w", encoding="utf-8") as f:
                f.write(report)
            
            print("Relatório de validação gerado em docs/reports/validation_report.md")

    except Exception as e:
        print(f"Erro na validação: {e}")

if __name__ == "__main__":
    asyncio.run(main())
