import logging
from typing import Any, Optional
from google.antigravity.hooks import hooks

class FallbackHook(hooks.OnToolErrorHook):
    """
    Guardrail: Intercepta erros de ferramentas e timeouts para evitar crashes abruptos
    e orientar o modelo a tentar alternativas ou devolver uma mensagem amigável ao usuário.
    """
    async def run(self, context: hooks.HookContext, data: Any) -> Optional[str]:
        # data representa a exceção capturada durante a execução de uma tool
        logging.error(f"Guardrail interceptou erro na ferramenta {context.tool_name}: {data}")
        
        if isinstance(data, (TimeoutError, ConnectionError)):
            return "[Erro de conexão com o serviço subjacente. Por favor, resuma o que foi feito até agora e informe ao usuário sobre a instabilidade de rede.]"
        
        if isinstance(data, ValueError):
             return "[Não foi possível completar a operação com os parâmetros fornecidos. Revise os argumentos e tente novamente ou informe o usuário.]"

        # Retorna uma mensagem genérica para erros inesperados
        return "[Ocorreu um erro interno ao processar a ferramenta. Comunique o usuário amigavelmente.]"

def get_base_config_kwargs() -> dict:
    """
    Retorna os parâmetros de configuração base (como os guardrails) 
    para serem injetados nos LocalAgentConfig de todos os agentes.
    Não usa Vertex AI (desvinculado do Google Cloud).
    """
    return {
        "hooks": [FallbackHook()],
    }
