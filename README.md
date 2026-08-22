# FinKnowledge Antigravity

Plataforma de Conhecimento Financeiro Auto-documentada com IA.
Projeto desenvolvido utilizando arquitetura Multiagentes com a SDK Google Antigravity, integrando um orquestrador base capaz de escalar o desenvolvimento e catalogar conhecimento corporativo.

## Pré-requisitos

Para rodar este projeto, você precisará de:
- [Docker](https://docs.docker.com/get-docker/) e [Docker Compose](https://docs.docker.com/compose/install/) (para a infraestrutura base de banco de dados, grafos e vetores)
- [Python 3.10+](https://www.python.org/downloads/) (para os serviços de API e Agentes)
- `make` instalado (geralmente padrão em ambientes Linux/macOS)

## Configuração Segura e Variáveis de Ambiente

Para manter o projeto seguro, garantimos que **nenhuma credencial de produção seja enviada para o repositório Git**. 
O arquivo `.gitignore` já está configurado para ignorar qualquer arquivo que inicie com `.env` (exceto o `.env.example`).

Para configurar seu ambiente local:

1. O comando `make setup` copiará o arquivo `.env.example` para `.env`. 
2. Abra o arquivo `.env` gerado e preencha suas chaves locais, especialmente a `GEMINI_API_KEY` para que os agentes (via Google Antigravity SDK) possam rodar localmente. Em produção ou outros ambientes, os provedores são agnósticos e baseados nos `.env` injetados.

## Instalação e Execução

Utilize os comandos do `Makefile` para facilitar a vida:

### 1. Setup Inicial
Este comando prepara as variáveis de ambiente e instala as dependências Python da API localmente:
```bash
make setup
```

### 2. Subir a Infraestrutura (Docker)
Este comando subirá o banco de dados (PostgreSQL + pgvector), Redis, Neo4j, Qdrant e MinIO localmente.
```bash
make up
```

*(Para derrubar a infraestrutura, utilize `make down`)*

### 3. Executando os Agentes e API
- **Para orquestrar multiagentes (testes locais):**
  ```bash
  python agents/orchestrator.py
  ```
- **Para subir a API (FastAPI):**
  ```bash
  PYTHONPATH=. python apps/api/main.py
  ```

## Estrutura do Projeto
- `apps/`: Contém APIs, admin web, etc.
- `agents/`: Contém o orquestrador e definições dos multiagentes (Architect, Planner, etc).
- `infra/`: Configurações declarativas para Docker Compose (uso local) e Helm/Terraform (prontas para produtivo).
- `knowledge/`: Catálogos, prompts e ontologias da plataforma.
- `docs/`: Documentação geral, ADRs e runbooks mantidos pela própria IA.

## Deploy Produtivo
O projeto já conta com arquivos de configuração separados em `infra/values-*.yaml`. Para subir em produção com infraestrutura conteinerizada real (ex: Kubernetes via Helm):
```bash
make deploy-prod
```
Os segredos em produção deverão ser injetados via CI/CD, sem depender de `.env` em repositório.
