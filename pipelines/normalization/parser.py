from apps.workers.celery_app import celery_app
import pdfplumber
import io

@celery_app.task
def parse_document_task(source_id: str, doc_hash: str, raw_content_bytes: bytes = None):
    """
    Worker para extração de texto (Parser).
    Recebe o conteúdo bruto (em produção, o path no S3/MinIO) e extrai o texto limpo.
    """
    print(f"[{doc_hash}] Iniciando Parser...")
    
    extracted_text = ""
    
    # Se tivéssemos baixado o PDF no passo anterior
    if raw_content_bytes:
        try:
            with pdfplumber.open(io.BytesIO(raw_content_bytes)) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        extracted_text += text + "\n"
        except Exception as e:
            print(f"[{doc_hash}] Falha ao fazer parse do PDF: {e}")
            return {"status": "error", "message": str(e)}
    else:
        # Mock para fluxo sem arquivo de fato (POC)
        extracted_text = "Art. 1º Fica regulamentado o crédito consignado INSS...\nParágrafo único. A margem consignável é de 35%."

    print(f"[{doc_hash}] Parsing concluído. Texto extraído: {len(extracted_text)} caracteres.")
    
    # Próximo passo da Pipeline: IA de Classificação
    from pipelines.classification.classifier_agent import classify_document_task
    classify_document_task.delay(doc_hash, extracted_text)
    
    return {"status": "success", "extracted_length": len(extracted_text)}
