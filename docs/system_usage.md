# FinKnowledge Antigravity - Manual de Uso do Sistema

Este documento descreve a arquitetura macro do sistema e detalha as responsabilidades entre Inteligência Artificial e a interação Humana, baseado no conceito de Multi-agentes com o Google Antigravity SDK.

## Arquitetura do Sistema (C4 Model)

```mermaid
C4Context
  title FinKnowledge Antigravity - Contexto de Sistema Multi-agentes

  Person(humano, "Usuário / Especialista", "Usuários de negócios, arquitetos, engenheiros de dados e compliance.")
  System(finknowledge, "FinKnowledge Platform", "Plataforma central que orquestra agentes, APIs e Graph/Vector Databases.")
  
  System_Ext(external_sources, "Fontes Externas", "Sistemas do BACEN, CMN e bases internas do banco.")

  Rel(humano, finknowledge, "Faz perguntas, revisa documentações, aprova normativos e gerencia prompts.")
  Rel(finknowledge, external_sources, "Ingere normativos, OpenAPI specs e metadados de código.")
```

### Containers (Macro-Visão)

```mermaid
C4Container
  title FinKnowledge Antigravity - Containers

  Person(humano, "Usuário", "Interage com o sistema.")

  Container_Boundary(c1, "Plataforma FinKnowledge") {
    Container(api, "API Gateway (FastAPI)", "Python", "Gerencia roteamento (Assistente, Taxonomia, Inventário, Prompts).")
    Container(orchestrator, "Orchestrator Agent", "Python / Antigravity", "Recebe épicos e delega para subagentes.")
    
    Container_Boundary(c2, "Subagentes (IA)") {
      Container(rag_agent, "RAG Agent", "Pesquisa semântica de normas.")
      Container(regulatory_agent, "Regulatory Agent", "Compara normas e extrai obrigações.")
      Container(architect_agent, "Architect Agent", "Sugere bounded contexts e APIs.")
      Container(qa_agent, "QA Agent", "Gera cenários de testes.")
      Container(doc_agent, "Doc Agent", "Gera e atualiza documentações (ADR, C4, README).")
      Container(trace_agent, "Trace Agent", "Ingere OpenAPI no Grafo.")
      Container(pm_agent, "PM Agent", "Quebra épicos em tarefas.")
      Container(trend_agent, "Trend Agent", "Monitora inovações de mercado.")
      Container(gap_agent, "Gap Agent", "Analisa lacunas do produto.")
      Container(sim_agent, "Simulator Agent", "Arquiteta simulações de novos produtos.")
      Container(eval_agent, "Eval Agent", "Mede qualidade, toxidade e coesão das IAs.")
    }

    ContainerDb(rel_db, "Relational DB", "PostgreSQL", "Armazena Prompts, Modelos, Configurações.")
    ContainerDb(vector_db, "Vector DB", "Qdrant", "Armazena embeddings de documentos normativos.")
    ContainerDb(graph_db, "Graph DB", "Neo4j", "Armazena inventário e relacionamentos de capacidades/APIs.")
  }

  Rel(humano, api, "Chama endpoints HTTP")
  Rel(api, orchestrator, "Despacha requisições complexas de IA")
  Rel(api, rag_agent, "Chama RAG no endpoint de Assistente")
  Rel(orchestrator, rag_agent, "Delega buscas")
  Rel(orchestrator, regulatory_agent, "Delega compliance")
  Rel(orchestrator, architect_agent, "Delega arquitetura")
  Rel(orchestrator, qa_agent, "Delega testes")
  Rel(orchestrator, doc_agent, "Delega auto-documentação")
  Rel(orchestrator, pm_agent, "Delega planejamento")
  
  Rel(rag_agent, vector_db, "Busca contexto normativo")
  Rel(trace_agent, graph_db, "Registra rastreabilidade")
```

## Divisão de Responsabilidades (Humano vs IA)

A plataforma baseia-se num fluxo **"Human-in-the-Loop"**.

### Responsabilidades da IA
- **Monitoramento e Ingestão:** Buscar ativamente mudanças em fontes normativas e código.
- **Classificação e Extração:** Criar resumos, gerar vetores e extrair entidades usando o `parser` e `collector`.
- **Análise Arquitetural e de QA:** Sugerir estruturas, microserviços e cenários de testes automatizados com base nas regras de negócio.
- **Auto-Documentação:** Re-escrever documentações e gerar diagramas dinamicamente, enviando como Pull Requests.
- **Rastreabilidade (Graph):** Conectar endpoints, serviços e domínios automaticamente a partir de repositórios e OpenAPI.

### Responsabilidades do Humano
- **Curadoria Inicial:** Configurar os Prompts e Agentes através do *Prompt Registry*.
- **Validação Crítica:** O *Regulatory Agent* identifica itens de alto impacto regulatório. O Humano **deve** aprovar o relatório de impacto gerado antes da propagação no grafo.
- **Revisão de Arquitetura:** O *Architect Agent* sugere arquiteturas que devem ser validadas e refinadas por engenheiros Sêniores.
- **Merges e Deploys:** A IA apenas propõe e cria Pull Requests; a aprovação e deploy final continuam sob responsabilidade humana (Tech Leads).

---
*Gerado dinamicamente através do Antigravity IDE Agent para o projeto FinKnowledge Base.*
