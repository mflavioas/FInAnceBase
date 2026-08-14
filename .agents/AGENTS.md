# Regras do Projeto FInAnceBase

1. **Automação do Git**: Ao finalizar qualquer implementação de código ou entrega de fase neste repositório, o agente deve SEMPRE executar de forma autônoma o fluxo completo de commit e push (`git add .`, `git commit -m "..."`, e `git push`). O repositório já está configurado com autenticação local.
2. **Segurança**: Nunca comite chaves, tokens (PATs), ou arquivos contendo credenciais (como o arquivo `.env`). Eles devem ser ignorados adequadamente via `.gitignore`.
