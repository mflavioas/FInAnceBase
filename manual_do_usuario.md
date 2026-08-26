# Manual do Usuário - FinKnowledge Antigravity

Bem-vindo à **Plataforma de Conhecimento Financeiro Auto-documentada com IA**. 
Este documento é um guia abrangente criado para orientar desde usuários iniciantes até perfis técnicos avançados no entendimento, instalação e uso cotidiano do ecossistema.

---

## 1. Visão Geral e Pacotes do Projeto

A plataforma utiliza uma **arquitetura de Multiagentes** (baseada na SDK Google Antigravity), onde diferentes "IAs" (agentes) possuem papéis específicos e trabalham juntas, orquestradas por um agente central. 

Aqui está o resumo dos principais módulos e pacotes:

- **`apps/`**: Contém os aplicativos que fornecem interfaces (para humanos ou sistemas).
  - `api`: A API principal do projeto (criada em FastAPI) que intermedeia o contato do mundo externo com os agentes.
  - `chat-ui`: Interface de conversação focada no usuário final para interação amigável com a IA.
  - `web-admin`: Painel de controle para configurações e gerenciamento.
  - `workers`: Processos assíncronos e tarefas em background.

- **`agents/`**: O "cérebro" do projeto.
  - `orchestrator.py`: É o gerente principal, que recebe uma tarefa complexa e a quebra, delegando sub-tarefas para os agentes abaixo.
  - **Agentes Específicos**: `compliance-agent` (conformidade), `doc-agent` (documentação), `pm-agent` (gestão), `qa-agent` (qualidade), `rag-agent` (busca em base de conhecimento), `regulatory-agent`, `trend-agent`, entre outros.

- **`pipelines/`**: Fluxos de dados que preparam informações para a IA.
  - Contém etapas como `ingestion` (receber arquivos), `normalization` (padronizar formatos), `classification` e `evaluation`.

- **`infra/`**: Configurações de infraestrutura como código (bancos de dados, Docker, Redis, Neo4j, Qdrant).
- **`knowledge/`**: Base local de catálogos e ontologias onde a estrutura lógica da IA se baseia.

---

## 2. Instalação e Configuração

Se você for rodar ou testar o projeto no seu computador, siga os passos abaixo.

### Pré-requisitos
- [Docker](https://docs.docker.com/get-docker/) e Docker Compose instalados.
- [Python 3.10+](https://www.python.org/downloads/).
- Utilitário `make` instalado (padrão em sistemas Linux e macOS).
- [Google Cloud CLI (gcloud)](https://cloud.google.com/sdk/docs/install) instalado (necessário para autenticação no Vertex AI).

### Passo a Passo
1. **Setup Inicial (Dependências e Variáveis)**:
   Abra o terminal na raiz do projeto e execute:
   ```bash
   make setup
   ```
   *Isso instalará as dependências Python (para a API) e gerará o arquivo `.env` (que guarda senhas e chaves ocultas).*

2. **Autenticação no Google Cloud (Vertex AI)**:
   - A plataforma utiliza os recursos do Vertex AI, cobrando diretamente no seu projeto Google Cloud.
   > **Nota:** É necessário ter o Google Cloud CLI instalado. Se ainda não o tem, baixe e instale através da [documentação oficial do Google](https://cloud.google.com/sdk/docs/install) antes de prosseguir.
   - No terminal da sua máquina, faça login rodando:
     ```bash
     gcloud auth application-default login
     ```
   - No arquivo `.env` na raiz do projeto, preencha as configurações correspondentes:
     `GOOGLE_CLOUD_PROJECT=seu-projeto`
     `GOOGLE_CLOUD_LOCATION=us-central1`
   *(Lembre-se: por segurança, esse arquivo `.env` nunca vai para o servidor central Git e não deve ser compartilhado).*

3. **Subindo os Bancos de Dados**:
   Inicialize todos os bancos de dados vetoriais, relacionais e grafos em background:
   ```bash
   make up
   ```

4. **Iniciando a Plataforma**:
   - Em um terminal, inicie a API:
     ```bash
     PYTHONPATH=. python apps/api/main.py
     ```
   - Em outros terminais, inicie as interfaces de usuário (front-end) rodando os comandos dentro de seus respectivos diretórios:
     - **Chat UI**: 
       ```bash
       cd apps/chat-ui
       npm install && npm run dev
       ```
       O chat estará disponível em **`http://localhost:3000`**.
     - **Web Admin**: 
       ```bash
       cd apps/web-admin
       npm install && npm run dev
       ```
       O painel administrativo estará disponível em **`http://localhost:3001`**.
     
     *(Nota: Se os diretórios estiverem vazios no repositório local, significa que o código do front-end ainda será enviado. Neste caso, continue os testes usando a documentação da API em `http://localhost:8000/docs` ou o terminal de orquestração).*
   - Caso queira testar a inteligência via terminal de orquestração (modo desenvolvedor):
     ```bash
     python agents/orchestrator.py
     ```

*(Para desligar a infraestrutura local, basta rodar `make down`).*

---

## 3. Guia de Uso por Perfis (Como Iniciar o Trabalho)

O sistema se adapta às suas necessidades e nível de conhecimento técnico:

### 👤 Perfil: Operador / Assistente (End-User Júnior)
- **Objetivo**: Fazer upload de documentos, cadastros e consultas de rotina.
- **Como Subir Documentos**: Utilize a interface Web (ou via chamada na API) para fazer upload de contratos, PDFs de relatórios financeiros e normativas. No momento do envio, o pacote `pipelines/ingestion` cuida de ler os arquivos de forma invisível para você.
- **Consultas Simples**: Pelo `chat-ui`, pergunte de forma natural, por exemplo: *"Faça um resumo do contrato da empresa X enviado ontem"*. O orquestrador entenderá e devolverá uma resposta coesa.

### 💼 Perfil: Analista Financeiro / de Negócios (Avançado)
- **Objetivo**: Extrair insights, validar conformidades e analisar dados históricos ou regulatórios.
- **Uso no Dia a Dia com IA**: Como os dados são indexados nos bancos de Grafos (Neo4j) e Vetores (Qdrant), você pode realizar perguntas analíticas complexas: *"Existem conflitos de conformidade nas movimentações de Maio segundo as novas normativas?"*.
- O `orchestrator` ativará o `compliance-agent` e o `rag-agent` para varrer todo o conhecimento indexado, buscando apenas a verdade baseada nos seus dados organizacionais.

### 🛠️ Perfil: Engenheiro / Administrador de Sistema (Dev)
- **Objetivo**: Monitorar infraestrutura, realizar *deploys* e evoluir os agentes.
- **Configurações e Deploy**: Use o módulo `web-admin` para gerir acessos e variáveis. Para mandar o projeto para produção em provedores na nuvem (Kubernetes/Helm), execute:
  ```bash
  make deploy-prod
  ```
- **Customização de IAs**: Novos fluxos ou agentes podem ser instanciados clonando estruturas da pasta `agents/` e adicionando sua etapa nas `pipelines/`.

---

## 4. Boas Práticas e IA no Dia a Dia

- **Seja Específico com a IA**: Quanto melhor for o detalhamento de sua pergunta no Chat, melhor a IA conseguirá delegar aos Agentes específicos. Ex: Em vez de dizer *"Verifique as métricas"*, diga *"Peça ao agente QA para verificar a qualidade das métricas trimestrais de TI"*.
- **Confiabilidade Anti-alucinação**: O coração deste projeto baseia-se na técnica de **RAG (Geração Aumentada por Recuperação)**. Isso significa que as respostas geradas são pautadas fortemente nos documentos reais em seu banco de dados, inibindo respostas inventadas pela IA.
- **Segurança e Commits (Aviso Importante)**: Ao codificar ou configurar a aplicação, nunca comite arquivos de ambiente (como `.env`) no GitHub ou versão chaves de API expostas em código. O projeto já é protegido no `.gitignore` para bloquear esse risco por padrão.
