# FinKnowledge - Runbook de Operações em Produção

Este documento consolida as práticas para manter a plataforma ativa, segura e íntegra (Fase 7).

## 1. Segurança e Acessos (RBAC)
A plataforma utiliza JWT via OAuth2PasswordBearer.
- Usuários comuns possuem a role `viewer` ou `curator`.
- Endpoints de Governança (`/governance/*`) exigem estritamente a role `admin`.

## 2. Backups (Disaster Recovery)
É responsabilidade da infraestrutura rodar os dumps diariamente.
Para executar o backup completo local:
```bash
bash scripts/backup.sh
```
Isso vai gerar um dump `.sql` do PostgreSQL e solicitar um snapshot à API do Qdrant.

## 3. Qualidade e Avaliação de IA
O Agente Avaliador (`Eval Agent`) deve ser acionado periodicamente (via Cron) para gerar métricas e gravar na tabela `ai_evaluations`.
O painel de monitoramento consumirá da rota `/governance/ai-evaluations` para plotar tendências de toxicidade e alucinação.

## 4. SLA e Manutenção
- **FastAPI**: Rodando via Uvicorn. Recomenda-se Gunicorn com workers uvicorn em Produção.
- **Banco de Dados**: Configurar o `max_connections` do PostgreSQL para 200, dado o modelo de multi-agentes.
