from apps.workers.celery_app import celery_app
import requests
import hashlib
from db.models import SourceType

@celery_app.task
def collect_source_task(source_id: str, source_url: str, source_type: str):
    """
    Coleta o conteúdo bruto de uma fonte.
    - Baixa o conteúdo (HTML, PDF).
    - Gera hash para verificar duplicidade ou versão nova.
    - Desencadeia o parser.
    """
    print(f"[{source_id}] Coletando de {source_url} ({source_type})")
    
    try:
        response = requests.get(source_url, timeout=30)
        response.raise_for_status()
        raw_content = response.content
        
        # Simulação de Hash para versão
        doc_hash = hashlib.sha256(raw_content).hexdigest()
        
        print(f"[{source_id}] Download concluído. Hash: {doc_hash}")
        
        # O próximo passo na pipeline seria gravar no Storage/MinIO
        # e então enfileirar o parsing
        from pipelines.normalization.parser import parse_document_task
        parse_document_task.delay(source_id, doc_hash)
        
        return {"status": "success", "hash": doc_hash}
    except Exception as e:
        print(f"[{source_id}] Falha ao coletar fonte: {e}")
        return {"status": "error", "message": str(e)}
