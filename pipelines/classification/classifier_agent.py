from apps.workers.celery_app import celery_app
from google.antigravity import Agent, LocalAgentConfig
import asyncio

# Configuração agnóstica para Antigravity via SDK
# Utilizará a GEMINI_API_KEY se fornecida
config = LocalAgentConfig(
    system_instruction="""
    Você é um Classificador de Normas do domínio financeiro.
    Sua missão é ler o trecho de um documento, extrair sua ementa principal,
    e classificá-lo em uma destas modalidades de crédito: 
    [CONSIGNADO_INSS, CONSIGNADO_SIAPE, CREDITO_PESSOAL, CARTAO_CONSIGNADO, FGTS, OUTROS].
    Retorne um JSON contendo {"modalidade": "...", "ementa": "...", "confianca": 0.0 a 1.0}
    """
)

@celery_app.task
def classify_document_task(doc_hash: str, text: str):
    """
    Utiliza Agente IA (Antigravity SDK) para classificar o texto e extrair metadados.
    """
    print(f"[{doc_hash}] Iniciando Classificação por IA...")
    
    # Wrap assíncrono para rodar o agente dentro do worker Celery Síncrono
    def _run_agent():
        async def _run():
            async with Agent(config) as agent:
                # Limitamos o tamanho do texto enviado para demonstração
                response = await agent.chat(text[:2000])
                return await response.text()
        return asyncio.run(_run())

    try:
        result_json_str = _run_agent()
        print(f"[{doc_hash}] Classificação Concluída: {result_json_str}")
        
        # Último passo da pipeline da Fase 1 seria gravar isso no PostgreSQL
        # mudando o status para PENDING_REVIEW (Curadoria Humana)
        return {"status": "success", "metadata": result_json_str}
        
    except Exception as e:
        print(f"[{doc_hash}] Erro na Classificação IA: {e}")
        return {"status": "error", "message": str(e)}
