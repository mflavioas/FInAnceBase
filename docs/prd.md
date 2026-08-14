# PRD — Plataforma de Conhecimento Financeiro Auto-documentada com IA  
## Projeto: FinKnowledge Antigravity  
**Versão:** 1.0  
**Status:** Em aprovação  
**Responsável:** Produto / Arquitetura / Antigravity AI Factory  
**Tema:** Base de conhecimento financeiro, regulatório, arquitetural e de produto para crédito brasileiro, com foco em crédito consignado, análise de tendências, gap analysis e geração assistida por IA.

---

## 1. Resumo Executivo

Este PRD define a construção de uma plataforma de conhecimento orientada por IA para catalogar, estruturar e operacionalizar regras de negócio, normas regulatórias, domínios de produto, arquitetura de software e inventário de sistemas financeiros.

O objetivo é permitir que a fábrica de software, usando **Antigravity + IA**, consiga:

- mapear produtos financeiros, como empréstimo consignado;
- identificar bounded contexts, capacidades e serviços necessários;
- comparar o que está previsto na base regulatória/negócio com o que já está construído;
- gerar planos de projeto, épicos, user stories, tarefas técnicas e testes;
- analisar tendências e novos produtos;
- manter documentação automaticamente atualizada pela própria IA;
- instalar e migrar facilmente entre ambiente local, desenvolvimento e produção.

A plataforma deve funcionar como um **cérebro de negócio e arquitetura** para apoiar decisões de produto, engenharia, compliance e inovação.

---

## 2. Objetivo do Produto

Criar uma plataforma auto-documentada, baseada em IA, que permita:

1. **Ingerir conhecimento regulatório e de negócio**  
   Exemplos: Banco Central, CMN, leis federais, INSS, Dataprev, FGTS, FEBRABAN, ANBIMA, manuais SCR, COSIF, políticas internas.

2. **Estruturar esse conhecimento em uma ontologia financeira**  
   Relacionando:
   - produto;
   - modalidade;
   - carteira;
   - convênio;
   - norma;
   - regra de negócio;
   - capacidade;
   - bounded context;
   - serviço;
   - API;
   - evento;
   - teste;
   - controle;
   - evidência.

3. **Permitir análise de domínio e arquitetura**  
   Exemplo:  
   “Quais contextos delimitados existem no domínio de consignado?”

4. **Permitir análise Base vs Construído**  
   Exemplo:  
   “O que já está implementado no sistema para o fluxo de averbação INSS?”

5. **Permitir análise de tendências e novos produtos**  
   Exemplo:  
   “Quais capacidades são necessárias para lançar cartão consignado INSS?”

6. **Gerar documentação automaticamente**  
   A IA deve produzir e manter:
   - ADRs;
   - dicionário de dados;
   - glossário;
   - documentação de APIs;
   - runbooks;
   - matrizes de rastreabilidade;
   - decisões de arquitetura;
   - evidências de teste;
   - impacto regulatório.

7. **Ser fácil de instalar, migrar e operar**  
   Deve haver:
   - ambiente local simples;
   - docker compose;
   - scripts de seed;
   - migração para produção com IaC;
   - backup/restore;
   - observabilidade;
   - segurança mínima.

---

## 3. Escopo

### 3.1 Dentro do escopo

- Modelagem da ontologia de crédito financeiro brasileiro;
- ingestão de normas, manuais, leis e documentos internos;
- armazenamento vetorial para busca semântica;
- grafo de conhecimento para relações entre entidades;
- catálogo de produtos, modalidades, carteiras e convênios;
- catálogo de bounded contexts e capacidades de domínio;
- inventário de serviços, APIs, eventos e repositórios;
- geração de matrizes “Base vs Construído”;
- agentes de IA para análise de produto, arquitetura, QA e compliance;
- auto-documentação assistida por IA;
- ambientes locais e produtivos portáveis;
- trilha de auditoria e controle de acesso.

### 3.2 Fora do escopo inicial

- execução automática de código em produção sem revisão humana;
- substituição de sistemas core bancários;
- envio automático de regulatórios ao Banco Central;
- integração real completa com Dataprev, INSS, Caixa ou registradoras no MVP;
- motor de crédito transacional completo;
- contabilidade fiscal completa;
- recomendações jurídicas finais sem validação humana.

---

## 4. Personas

### 4.1 Product Manager / Product Owner

Quer entender quais capacidades são necessárias para um novo produto, priorizar backlog e avaliar impacto de mudanças regulatórias.

### 4.2 Arquiteto de Software

Quer mapear bounded contexts, serviços, APIs, eventos, dependências e impactos técnicos.

### 4.3 Engenheiro de Software

Quer consultar regras de negócio, normas associadas, APIs existentes e gerar tarefas ou código com contexto correto.

### 4.4 Analista Regulatório / Compliance

Quer rastrear quais normas impactam produtos, serviços e controles.

### 4.5 QA / Quality Engineer

Quer gerar cenários de teste baseados em regras regulatórias e fluxos de negócio.

### 4.6 Gestor de Fábrica / Líder de Delivery

Quer visão de gaps, riscos, esforço, status de implementação e oportunidades de reuso.

### 4.7 Agente IA / Antigravity

Atua como executor assistido, gerando código, documentação, análise, testes e sugestões de arquitetura a partir da base de conhecimento.

---

## 5. Princípios do Produto

### 5.1 Knowledge-first

Toda funcionalidade, geração de código ou análise deve buscar contexto na base de conhecimento.

### 5.2 Self-documenting

A IA deve registrar decisões, alterações, artefatos e evidências automaticamente.

### 5.3 Traceability

Toda regra importante deve ser rastreável entre:

```text
Norma → Regra → Capacidade → Contexto → Serviço → Código → Teste → Evidência
```

### 5.4 Human-in-the-loop

A IA sugere, analisa e documenta, mas decisões regulatórias, jurídicas e críticas devem ser aprovadas por humanos.

### 5.5 Portability

A solução deve ser fácil de executar localmente e migrar para produção.

### 5.6 Modularity

A plataforma deve ser composta por serviços independentes e substituíveis.

### 5.7 Auditability

Toda consulta, geração, alteração e ingestão deve possuir trilha auditável.

### 5.8 Security by design

Dados sensíveis, tokens, chaves e documentos devem respeitar LGPD e boas práticas de segurança.

---

## 6. Arquitetura de Referência

## 6.1 Camadas da Plataforma

```text
┌─────────────────────────────────────────────────────────────┐
│                       Camada de Consumo                     │
│ Chat IA, Dashboards, API, IDE/Agentes Antigravity, CLI      │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│                     Camada de Agentes IA                    │
│ Agente de Produto, Arquitetura, Compliance, QA, Tendências  │
│ Agente de Documentação, Gap Analysis, Impact Analysis       │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│                  Camada de Conhecimento                     │
│ Ontologia, Taxonomia, Grafo, Vetores, Catálogos, Regras     │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│                  Camada de Ingestão                         │
│ Coletores, Parsers, Normalização, Classificação, Curadoria  │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│                  Camada de Infraestrutura                   │
│ Postgres/pgvector, Neo4j, MinIO/S3, Fila, Observability     │
└─────────────────────────────────────────────────────────────┘
```

---

## 6.2 Componentes principais

| Componente | Responsabilidade |
|---|---|
| Ingestion Service | Coleta, extrai, normaliza e versiona documentos |
| Taxonomy Service | Gerencia taxonomia de produtos, modalidades, carteiras |
| Knowledge Graph Service | Mantém relações entre normas, regras, domínios e sistemas |
| Vector Search Service | Busca semântica sobre documentos |
| Inventory Service | Cataloga serviços, APIs, eventos, repositórios |
| Traceability Service | Liga requisitos, regras, código, testes e evidências |
| AI Agent Orchestrator | Orquestra agentes de IA |
| Self-Doc Service | Gera e mantém documentação automática |
| Admin UI | Interface para curadoria, catálogos e governança |
| Chat/Assistant UI | Interface conversacional |
| API Gateway | Exposição segura das APIs |
| Observability Stack | Logs, métricas, traces, auditoria |
| Auth Service | Autenticação, autorização e RBAC |

---

## 6.3 Stack recomendada para fácil instalação

### Ambiente local

Ferramentas sugeridas:

- Docker Compose;
- Makefile;
- Python 3.12+;
- FastAPI;
- PostgreSQL com pgvector;
- Qdrant ou pgvector para busca vetorial;
- Neo4j ou Memgraph para grafo;
- MinIO para objetos/documentos;
- Redis para fila/cache;
- Alembic para migrações SQL;
- pytest para testes;
- MkDocs ou Docusaurus para documentação gerada;
- Ollama opcional para modelos locais;
- OpenAI, Azure OpenAI, Anthropic ou outro provedor de IA.

Comandos esperados:

```bash
make setup
make up
make seed
make test
make docs
```

### Ambiente produtivo

Opções recomendadas:

- Kubernetes com Helm;
- Terraform para provisionar infraestrutura;
- PostgreSQL gerenciado;
- armazenamento S3 compatível;
- serviço de vetor gerenciado ou Qdrant em cluster;
- Neo4j gerenciado ou Postgres com extensão de grafo, se necessário;
- CI/CD com GitHub Actions, GitLab CI ou Azure DevOps;
- Vault ou Secret Manager;
- Keycloak ou provedor OIDC;
- OpenTelemetry, Prometheus, Grafana e Loki;
- backups automatizados;
- blue/green ou canary deployment.

---

## 7. Estratégia de Auto-documentação pela IA

A plataforma deve ser auto-documentada em múltiplos níveis.

## 7.1 Documentos gerados automaticamente

A IA deve gerar ou atualizar:

1. **ADR — Architecture Decision Records**  
   Sempre que uma decisão relevante for registrada.

2. **Data Dictionary**  
   Dicionário de entidades, tabelas, campos e relacionamentos.

3. **API Documentation**  
   Documentação OpenAPI/Swagger atualizada automaticamente.

4. **Glossário de Negócio**  
   Termos financeiros, regulatórios e técnicos.

5. **Matriz de Rastreabilidade**  
   Norma → regra → capacidade → serviço → teste.

6. **Runbooks Operacionais**  
   Procedimentos de deploy, backup, restore, incidentes e rollback.

7. **Relatórios de Gap**  
   Comparação entre base necessária e implementação atual.

8. **Relatórios de Impacto Regulatório**  
   Quais sistemas e processos são afetados por mudanças normativas.

9. **Prompt Registry**  
   Versionamento de prompts, agentes, modelos e parâmetros.

10. **Evidências de Teste**  
   Resultados de testes, cobertura e cenários validados.

---

## 7.2 Regras de auto-documentação

Toda mudança relevante deve registrar:

```yaml
change_id: UUID
timestamp: data/hora
author: usuário ou agente
type: feature|architecture|data|prompt|policy|bugfix
summary: descrição curta
impact:
  domains: []
  services: []
  regulations: []
artifacts:
  - api_spec
  - migration
  - test_report
  - adr
review:
  required: true
  approved_by:
```

---

## 8. Fases do Projeto

O projeto será dividido em fases para permitir evolução incremental e uso rápido de valor.

---

# Fase 0 — Bootstrap, Infraestrutura e Portabilidade

## Objetivo

Criar uma base técnica simples, instalável localmente e migrável para produção.

## Entregáveis

- repositório inicial;
- docker compose;
- Makefile;
- configuração de ambientes;
- migrações de banco;
- observabilidade básica;
- autenticação básica;
- documentação inicial gerada automaticamente.

---

## User Stories — Fase 0

### US-001 — Instalação local simplificada

**Como** engenheiro de software  
**quero** instalar a plataforma com poucos comandos  
**para** começar a usar o ambiente rapidamente.

#### Critérios de aceite

- Deve existir `docker-compose.yml` com serviços essenciais.
- Deve existir `.env.example`.
- Deve existir `Makefile` com comandos:
  - `make setup`
  - `make up`
  - `make down`
  - `make logs`
  - `make seed`
  - `make test`
- O ambiente deve subir:
  - API;
  - Postgres;
  - Vector store;
  - Graph store;
  - MinIO/S3 local;
  - Redis;
  - UI administrativa.
- O comando `make setup` deve validar dependências.
- O comando `make up` deve iniciar os serviços sem erro.
- A documentação local deve ser gerada após o bootstrap.

---

### US-002 — Configuração por ambiente

**Como** DevOps  
**quero** separar configurações de local, dev, staging e prod  
**para** evitar erros e facilitar migração.

#### Critérios de aceite

- Deve haver arquivos:
  - `.env.example`
  - `values-local.yaml`
  - `values-dev.yaml`
  - `values-prod.yaml`
- Segredos não devem ser versionados.
- Deve haver validação de variáveis obrigatórias.
- Deve haver suporte a provedores de IA configuráveis.
- O sistema deve falhar com mensagem clara se faltar configuração crítica.

---

### US-003 — Provisionamento para produção com IaC

**Como** arquiteto de plataforma  
**quero** provisionar a infraestrutura com Terraform ou similar  
**para** reproduzir produção de forma confiável.

#### Critérios de aceite

- Deve existir módulo Terraform ou template equivalente.
- Deve ser possível provisionar:
  - banco de dados;
  - armazenamento de objetos;
  - segredos;
  - rede básica;
  - serviço de aplicação;
  - monitoramento.
- Deve existir documentação de deploy.
- Deve existir script de validação pós-deploy.
- Deve haver plano de rollback documentado.

---

### US-004 — Observabilidade básica

**Como** operador  
**quero** visualizar logs, métricas e traces  
**para** diagnosticar problemas rapidamente.

#### Critérios de aceite

- Deve existir endpoint `/health`.
- Deve existir endpoint `/metrics`.
- Logs devem estar estruturados em JSON.
- Deve haver correlação por `trace_id`.
- Deve haver dashboard básico com:
  - status da API;
  - jobs de ingestão;
  - uso de banco;
  - latência de consultas à IA.
- Auditoria deve registrar ações críticas.

---

### US-005 — Boot de documentação automática

**Como** product manager  
**quero** que a IA gere uma documentação inicial do projeto  
**para** que o conhecimento não fique disperso.

#### Critérios de aceite

- Ao rodar `make docs`, a IA deve gerar:
  - README;
  - visão de arquitetura;
  - dicionário inicial de dados;
  - lista de serviços;
  - runbook local;
  - glossário inicial.
- A documentação deve ser versionada.
- A documentação deve indicar data de geração e versão do código.
- Deve haver índice pesquisável.

---

# Fase 1 — Ingestão e Normalização de Conhecimento

## Objetivo

Criar a base documental inicial com normas, manuais, leis, documentos internos e catálogos.

## Entregáveis

- conectores para fontes;
- pipeline de ingestão;
- parser de PDF/HTML/DOCX;
- extração de metadados;
- versionamento de normas;
- curadoria humana;
- trilha de auditoria.

---

## User Stories — Fase 1

### US-101 — Cadastro de fontes de conhecimento

**Como** curador de conhecimento  
**quero** cadastrar fontes oficiais e internas  
**para** que a IA saiba onde buscar documentos.

#### Critérios de aceite

- Deve ser possível cadastrar fontes com:
  - nome;
  - URL;
  - tipo;
  - entidade responsável;
  - frequência de coleta;
  - autenticação, se necessário;
  - domínio relacionado.
- Tipos de fonte suportados inicialmente:
  - BACEN;
  - CMN;
  - Planalto;
  - INSS/Dataprev;
  - FEBRABAN;
  - ANBIMA;
  - documentos internos;
  - manuais técnicos;
  - políticas internas.
- Cada fonte deve ter status ativa/inativa.
- Deve haver registro de última coleta.

---

### US-102 — Coleta automática de documentos

**Como** engenheiro de dados  
**quero** coletar documentos automaticamente das fontes cadastradas  
**para** manter a base atualizada.

#### Critérios de aceite

- Deve existir pipeline de coleta agendada.
- Deve suportar:
  - HTML;
  - PDF;
  - XML;
  - DOCX;
  - Markdown;
  - APIs JSON.
- Deve registrar hash do documento coletado.
- Deve detectar alterações entre versões.
- Deve armazenar arquivo bruto em storage.
- Deve registrar erros de coleta.

---

### US-103 — Extração estruturada de textos

**Como** curador  
**quero** que documentos sejam convertidos em texto estruturado  
**para** permitir busca e análise pela IA.

#### Critérios de aceite

- PDFs devem ser processados com OCR quando necessário.
- A extração deve preservar:
  - título;
  - ementa;
  - artigos;
  - incisos;
  - parágrafos;
  - anexos;
  - tabelas, quando possível.
- Deve existir metadado indicando confiabilidade da extração.
- Trechos não reconhecidos devem ser marcados para revisão.
- Deve haver pré-visualização para curadoria.

---

### US-104 — Classificação automática de documentos

**Como** product manager  
**quero** que a IA classifique documentos por produto, entidade e fase  
**para** organizar a base sem esforço manual.

#### Critérios de aceite

- A IA deve sugerir:
  - produto;
  - modalidade;
  - entidade reguladora;
  - fase do ciclo de crédito;
  - tipo documental;
  - criticidade.
- Deve haver confiança por classificação.
- Deve ser possível aprovar ou corrigir sugestões.
- Classificações aprovadas devem gerar trilha de auditoria.

---

### US-105 — Versionamento de normas e documentos

**Como** analista regulatório  
**quero** controlar versões de normas e documentos  
**para** saber o que mudou ao longo do tempo.

#### Critérios de aceite

- Cada documento deve possuir:
  - id;
  - versão;
  - data de publicação;
  - data de vigência;
  - status;
  - entidade;
  - link original;
  - hash;
  - texto extraído.
- Deve suportar relações:
  - altera;
  - revoga;
  - complementa;
  - regulamenta;
  - substitui.
- Deve haver comparação entre versões.
- Alterações devem gerar evento de conhecimento.

---

### US-106 — Curadoria humana

**Como** especialista de negócio  
**quero** revisar e aprovar documentos ingeridos  
**para** garantir qualidade da base.

#### Critérios de aceite

- Deve existir fila de revisão.
- Deve mostrar:
  - documento bruto;
  - texto extraído;
  - metadados sugeridos;
  - classificação da IA;
  - diferenças desde a última versão.
- O revisor pode aprovar, rejeitar ou ajustar.
- Nenhuma norma deve ser considerada válida sem aprovação humana.
- Toda decisão deve registrar autor, data e justificativa.

---

### US-107 — Trilha de auditoria da ingestão

**Como** compliance  
**quero** registrar todas as ações de ingestão  
**para** auditar alterações e origens.

#### Critérios de aceite

- Deve registrar:
  - coleta;
  - parser;
  - classificação;
  - revisão;
  - aprovação;
  - reprocessamento;
  - exclusão.
- Deve existir identificador de evento.
- Logs devem ser imutáveis ou protegidos contra edição.
- Deve ser possível exportar auditoria em CSV/JSON.

---

# Fase 2 — Taxonomia, Ontologia e Catálogos de Negócio

## Objetivo

Criar a estrutura conceitual do domínio financeiro.

## Entregáveis

- taxonomia de produtos;
- catálogo de modalidades;
- catálogo de carteiras;
- catálogo de convênios;
- ontologia de domínio;
- catálogo de capacidades;
- catálogo de bounded contexts.

---

## User Stories — Fase 2

### US-201 — Catálogo de produtos financeiros

**Como** product manager  
**quero** cadastrar produtos financeiros  
**para** organizar o conhecimento por linha de negócio.

#### Critérios de aceite

- Deve suportar produtos como:
  - crédito consignado;
  - crédito pessoal;
  - cartão consignado;
  - antecipação FGTS;
  - crédito com garantia;
  - financiamento.
- Cada produto deve possuir:
  - código;
  - nome;
  - família;
  - segmento;
  - status;
  - descrição;
  - normas relacionadas;
  - capacidades necessárias;
  - domínios afetados.
- Deve suportar hierarquia:
  - família;
  - produto;
  - modalidade;
  - submodalidade.

---

### US-202 — Catálogo de modalidades

**Como** arquiteto de produto  
**quero** cadastrar modalidades de crédito  
**para** reaproveitar regras entre produtos.

#### Critérios de aceite

- Cada modalidade deve conter:
  - código;
  - nome;
  - tipo de desconto;
  - segmento;
  - controlador de margem;
  - regras de teto;
  - prazo máximo;
  - exigência de averbação;
  - exigência de registro;
  - reportes regulatórios.
- Deve permitir regras parametrizadas.
- Deve permitir herança de regras de modalidade pai.

---

### US-203 — Catálogo de carteiras

**Como** gestor de risco  
**quero** cadastrar carteiras de crédito  
**para** associar políticas contábeis, regulatórias e de risco.

#### Critérios de aceite

- Cada carteira deve conter:
  - código;
  - nome;
  - modalidade;
  - política de risco;
  - política contábil;
  - política de provisão;
  - reportes obrigatórios;
  - critérios de aceitação.
- Deve permitir associação com produtos e convênios.
- Deve permitir status ativa, inativa, em migração.

---

### US-204 — Catálogo de convênios e entes pagadores

**Como** especialista em consignado  
**quero** cadastrar convênios  
**para** controlar regras específicas de averbação e margem.

#### Critérios de aceite

- Deve suportar:
  - INSS;
  - SIAPE;
  - estados;
  - municípios;
  - empresas privadas;
  - tribunais;
  - forças armadas;
  - outras entidades.
- Cada convênio deve conter:
  - código;
  - nome;
  - tipo;
  - canal de integração;
  - layouts suportados;
  - regras de margem;
  - limites de taxa;
  - prazo máximo;
  - status;
  - SLA;
  - documentos de referência.
- Deve permitir regras específicas por convênio.

---

### US-205 — Catálogo de capacidades de negócio

**Como** arquiteto  
**quero** catalogar capacidades de negócio  
**para** mapear o que cada produto precisa para funcionar.

#### Critérios de aceite

- Deve suportar níveis hierárquicos.
- Exemplo:
  - Crédito
    - Originação
      - Simulação
    - Controle de Margem
      - Reserva de Margem
- Cada capacidade deve ter:
  - id;
  - nome;
  - descrição;
  - domínio;
  - produtos relacionados;
  - normas relacionadas;
  - contexto relacionado;
  - status de implementação.

---

### US-206 — Catálogo de bounded contexts

**Como** arquiteto DDD  
**quero** catalogar bounded contexts  
**para** organizar limites de domínio.

#### Critérios de aceite

- Cada contexto deve conter:
  - id;
  - nome;
  - domínio;
  - descrição;
  - entidades;
  - eventos;
  - APIs;
  - serviços;
  - regras;
  - integrações;
  - dependências.
- Deve suportar visualização em mapa.
- Deve permitir relacionar contexto com capacidades.

---

### US-207 — Ontologia mínima do domínio financeiro

**Como** cientista de dados  
**quero** uma ontologia mínima  
**para** padronizar entidades e relações.

#### Critérios de aceite

- A ontologia deve conter entidades mínimas:
  - Product;
  - Modality;
  - Portfolio;
  - Agreement;
  - Regulation;
  - BusinessRule;
  - Capability;
  - BoundedContext;
  - Service;
  - API;
  - Event;
  - Test;
  - Control;
  - Evidence.
- Deve conter relações mínimas:
  - regulates;
  - implements;
  - affects;
  - requires;
  - belongs_to;
  - maps_to;
  - tested_by;
  - documented_by.
- Deve ser versionada.
- Deve permitir extensão sem quebrar dados existentes.

---

# Fase 3 — Grafo de Conhecimento e Busca Semântica

## Objetivo

Permitir consultas inteligentes, rastreabilidade e geração de análise por IA.

## Entregáveis

- banco vetorial;
- grafo de conhecimento;
- API de busca;
- busca com citações;
- consultas de impacto;
- RAG com trilha.

---

## User Stories — Fase 3

### US-301 — Indexação vetorial de documentos

**Como** usuário de negócio  
**quero** pesquisar normas e regras semanticamente  
**para** encontrar respostas rapidamente.

#### Critérios de aceite

- Documentos aprovados devem ser vetorizados.
- Cada chunk deve manter metadados:
  - documento;
  - seção;
  - artigo;
  - entidade;
  - produto;
  - domínio;
  - vigência.
- A busca deve retornar trechos com citação.
- Deve suportar filtro por produto, entidade e fase.
- Deve registrar consulta e resultado para auditoria.

---

### US-302 — Grafo de conhecimento

**Como** arquiteto  
**quero** consultar relações entre normas, regras e sistemas  
**para** entender impactos.

#### Critérios de aceite

- Deve armazenar nós e arestas conforme ontologia.
- Deve suportar consultas como:
  - “quais serviços implementam esta regra?”
  - “quais normas afetam este contexto?”
  - “quais capacidades faltam para este produto?”
- Deve existir API para criar, atualizar e consultar nós.
- Alterações devem ser versionadas.
- Deve haver visualização gráfica simples.

---

### US-303 — Resposta com citação obrigatória

**Como** compliance officer  
**quero** que respostas da IA citem fontes  
**para** validar a origem da informação.

#### Critérios de aceite

- Toda resposta regulatória deve citar:
  - documento;
  - trecho;
  - link;
  - versão;
  - data de vigência.
- Se não houver fonte suficiente, a IA deve dizer que não sabe.
- Deve haver nível de confiança.
- Respostas sem citação devem ser marcadas como não verificadas.

---

### US-304 — Consulta de impacto regulatório

**Como** analista regulatório  
**quero** perguntar quais objetos são afetados por uma norma  
**para** planejar mudanças.

#### Critérios de aceite

- Deve suportar perguntas como:
  - “quais serviços são afetados pela norma X?”
  - “quais testes cobrem a regra Y?”
  - “quais produtos dependem da margem INSS?”
- A resposta deve retornar:
  - entidades afetadas;
  - severidade;
  - evidências;
  - recomendações.
- Deve permitir exportar relatório em Markdown/PDF/JSON.

---

### US-305 — RAG com controle de acesso

**Como** administrador  
**quero** que usuários só consultem documentos permitidos  
**para** respeitar segurança e LGPD.

#### Critérios de aceite

- Documentos devem ter nível de acesso.
- Busca deve filtrar por permissão do usuário.
- Agentes IA devem respeitar o mesmo controle.
- Deve haver log de acesso a documentos sensíveis.

---

# Fase 4 — Inventário de Sistemas e Rastreabilidade

## Objetivo

Conectar o conhecimento de negócio ao que realmente está construído.

## Entregáveis

- catálogo de serviços;
- catálogo de APIs;
- catálogo de eventos;
- catálogo de repositórios;
- matriz base vs construído;
- rastreamento norma → código.

---

## User Stories — Fase 4

### US-401 — Catálogo de serviços

**Como** arquiteto  
**quero** cadastrar serviços existentes  
**para** mapear a arquitetura atual.

#### Critérios de aceite

- Cada serviço deve conter:
  - nome;
  - domínio;
  - responsável;
  - repositório;
  - APIs;
  - eventos;
  - bancos de dados;
  - dependências;
  - status.
- Deve permitir importação manual e automática.
- Deve suportar tags por produto e capacidade.

---

### US-402 — Importação de especificações OpenAPI

**Como** engenheiro de software  
**quero** importar arquivos OpenAPI  
**para** popular o catálogo de APIs automaticamente.

#### Critérios de aceite

- Deve aceitar Swagger/OpenAPI 3.x.
- Deve extrair:
  - endpoints;
  - métodos;
  - schemas;
  - autenticação;
  - versões.
- Deve sugerir associação com bounded contexts.
- Deve detectar breaking changes entre versões.
- Deve gerar documentação automaticamente.

---

### US-403 — Importação de repositórios e pipelines

**Como** DevOps  
**quero** conectar repositórios Git  
**para** rastrear código relacionado a capacidades.

#### Critérios de aceite

- Deve suportar GitHub, GitLab ou Azure DevOps.
- Deve ler metadados como:
  - README;
  - CI config;
  - Dockerfile;
  - Helm charts;
  - migrations;
  - testes.
- Deve sugerir relacionamento com serviços e capacidades.
- Deve respeitar permissões de acesso.

---

### US-404 — Matriz Base vs Construído

**Como** gestor de fábrica  
**quero** visualizar o que está previsto e o que está implementado  
**para** identificar gaps.

#### Critérios de aceite

- Deve gerar matriz com:
  - domínio;
  - capacidade;
  - contexto;
  - requisito regulatório;
  - serviço;
  - API;
  - teste;
  - status.
- Status deve ser:
  - não iniciado;
  - parcial;
  - implementado;
  - validado;
  - depreciado.
- Deve permitir drill-down até código/documento.
- Deve permitir exportação para CSV/PDF.

---

### US-405 — Rastreabilidade de regra para código

**Como** QA  
**quero** ligar regras a testes e código  
**para** validar cobertura.

#### Critérios de aceite

- Deve permitir associar regra a:
  - serviço;
  - endpoint;
  - função;
  - teste;
  - evidência.
- Deve mostrar cobertura por regra.
- Deve alertar regras críticas sem teste.
- Deve registrar histórico de associações.

---

# Fase 5 — Agentes de IA e Workflows

## Objetivo

Criar agentes especializados para apoiar produto, arquitetura, QA, compliance e documentação.

## Entregáveis

- orquestrador de agentes;
- chat com contexto;
- geração de épicos;
- geração de arquitetura;
- geração de testes;
- análise de tendências;
- auto-documentação.

---

## User Stories — Fase 5

### US-501 — Assistente conversacional de conhecimento financeiro

**Como** usuário de negócio  
**quero** conversar com a IA sobre regras e produtos  
**para** obter respostas confiáveis com fontes.

#### Critérios de aceite

- Deve responder com base no knowledge graph e RAG.
- Deve citar documentos.
- Deve permitir filtros por produto, domínio e entidade.
- Deve manter histórico da conversa.
- Deve permitir salvar consultas importantes.

---

### US-502 — Agente arquiteto

**Como** arquiteto  
**quero** que a IA gere propostas de arquitetura  
**para** novos produtos ou mudanças.

#### Critérios de aceite

- Deve gerar:
  - bounded contexts;
  - serviços sugeridos;
  - eventos;
  - APIs;
  - integrações;
  - riscos;
  - dependências.
- Deve se basear em capacidades já catalogadas.
- Deve indicar reuso de domínios compartilhados.
- Deve gerar ADR inicial.

---

### US-503 — Agente product manager

**Como** product manager  
**quero** que a IA gere épicos e user stories  
**para** novos produtos.

#### Critérios de aceite

- Deve gerar backlog com:
  - épicos;
  - features;
  - user stories;
  - critérios de aceite;
  - dependências;
  - riscos;
  - estimativa preliminar.
- Deve considerar lacunas identificadas.
- Deve sugerir MVP.
- Deve permitir exportar para Jira/Azure DevOps.

---

### US-504 — Agente regulatório

**Como** compliance  
**quero** que a IA analise mudanças normativas  
**para** identificar impactos.

#### Critérios de aceite

- Deve comparar versão anterior e nova da norma.
- Deve extrair obrigações.
- Deve relacionar com produtos e serviços.
- Deve gerar relatório de impacto.
- Deve marcar itens que exigem validação humana.

---

### US-505 — Agente QA

**Como** QA  
**quero** gerar cenários de teste a partir de regras  
**para** aumentar cobertura.

#### Critérios de aceite

- Deve gerar cenários funcionais e não funcionais.
- Deve considerar regras regulatórias.
- Deve gerar exemplos de dados.
- Deve sugerir testes automatizados.
- Deve vincular cenários a regras e capacidades.

---

### US-506 — Agente de documentação automática

**Como** tech lead  
**quero** que a IA atualize documentação após mudanças  
**para** evitar documentação obsoleta.

#### Critérios de aceite

- Deve gerar/atualizar:
  - README;
  - ADRs;
  - dicionário de dados;
  - API docs;
  - runbooks;
  - changelog.
- Deve detectar mudanças em código, schema e prompts.
- Deve abrir pull request de documentação.
- Deve registrar evidência de atualização.

---

### US-507 — Prompt registry

**Como** engenheiro de IA  
**quero** versionar prompts e configurações de agentes  
**para** auditoria e reprodutibilidade.

#### Critérios de aceite

- Cada prompt deve possuir:
  - id;
  - versão;
  - objetivo;
  - modelo;
  - parâmetros;
  - testes;
  - dono;
  - status.
- Deve permitir testes A/B ou avaliação.
- Deve registrar uso em produção.
- Deve permitir rollback para versão anterior.

---

# Fase 6 — Análise de Tendências, Gap Analysis e Novos Produtos

## Objetivo

Transformar a base em ferramenta de inovação e planejamento.

## Entregáveis

- radar de tendências;
- análise de lacunas;
- simulador de novo produto;
- recomendação de reuso;
- roadmap orientado por risco.

---

## User Stories — Fase 6

### US-601 — Radar de tendências

**Como** head de inovação  
**quero** acompanhar tendências financeiras e regulatórias  
**para** identificar oportunidades.

#### Critérios de aceite

- Deve coletar fontes externas aprovadas.
- Deve classificar tendências por:
  - produto;
  - tecnologia;
  - regulação;
  - experiência;
  - risco.
- Deve gerar score de relevância.
- Deve indicar domínios afetados.
- Deve permitir curadoria humana.

---

### US-602 — Análise de gap por produto

**Como** product manager  
**quero** saber o que falta para um produto funcionar  
**para** priorizar backlog.

#### Critérios de aceite

- Deve comparar capacidades necessárias vs implementadas.
- Deve mostrar:
  - lacunas funcionais;
  - lacunas técnicas;
  - lacunas regulatórias;
  - lacunas de teste;
  - lacunas de integração.
- Deve priorizar por risco e valor.
- Deve sugerir épicos para fechar gaps.

---

### US-603 — Simulador de novo produto

**Como** arquiteto de produto  
**quero** simular a criação de um novo produto  
**para** entender requisitos e esforço.

#### Critérios de aceite

- Usuário deve informar parâmetros mínimos:
  - família;
  - modalidade;
  - segmento;
  - forma de desconto;
  - garantias;
  - canal;
  - integração necessária.
- A IA deve gerar:
  - capacidades necessárias;
  - contextos;
  - normas prováveis;
  - integrações;
  - riscos;
  - backlog sugerido.
- Deve indicar o que pode ser reaproveitado.
- Deve gerar documento de viabilidade inicial.

---

### US-604 — Recomendação de reuso

**Como** arquiteto  
**quero** receber sugestões de domínios compartilhados  
**para** evitar retrabalho.

#### Critérios de aceite

- A IA deve identificar capacidades semelhantes entre produtos.
- Deve sugerir:
  - serviços compartilhados;
  - catálogos centrais;
  - eventos comuns;
  - regras parametrizáveis.
- Deve mostrar ganho estimado de reuso.
- Deve permitir aprovar ou recusar sugestões com justificativa.

---

# Fase 7 — Produção, Governança, Segurança e Qualidade

## Objetivo

Tornar a plataforma confiável, segura e operacional.

## Entregáveis

- RBAC;
- auditoria completa;
- backup/restore;
- qualidade de dados;
- avaliação de IA;
- SLA;
- runbooks produtivos.

---

## User Stories — Fase 7

### US-701 — Autenticação e autorização

**Como** administrador  
**quero** controlar acesso por papéis  
**para** proteger dados sensíveis.

#### Critérios de aceite

- Deve suportar OIDC/OAuth2.
- Deve ter papéis mínimos:
  - admin;
  - curador;
  - product manager;
  - arquiteto;
  - engenheiro;
  - compliance;
  - leitor.
- Permissões devem valer para UI, API e agentes IA.
- Deve registrar login e ações críticas.

---

### US-702 — Backup e restore

**Como** operador  
**quero** realizar backup dos dados  
**para** evitar perda de conhecimento.

#### Critérios de aceite

- Backup deve incluir:
  - banco relacional;
  - índice vetorial;
  - grafo;
  - arquivos;
  - configurações;
  - prompt registry.
- Deve haver rotina automática.
- Deve haver teste de restore.
- Deve haver documentação de recuperação.

---

### US-703 — Qualidade de dados

**Como** curador  
**quero** monitorar qualidade da base  
**para** evitar respostas incorretas.

#### Critérios de aceite

- Deve monitorar:
  - documentos sem classificação;
  - normas vencidas;
  - regras sem teste;
  - serviços sem dono;
  - entidades órfãs;
  - citações quebradas.
- Deve gerar painel de qualidade.
- Deve criar tarefas de correção automaticamente.

---

### US-704 — Avaliação de respostas de IA

**Como** engenheiro de IA  
**quero** medir qualidade das respostas  
**para** reduzir alucinações.

#### Critérios de aceite

- Deve existir conjunto de perguntas douradas.
- Deve medir:
  - relevância;
  - fidelidade à fonte;
  - completude;
  - citação correta;
  - risco regulatório.
- Deve registrar métricas por versão de prompt/modelo.
- Deve bloquear promoção de agentes com score abaixo do limite.

---

### US-705 — Runbooks e resposta a incidentes

**Como** SRE  
**quero** runbooks gerados e atualizados  
**para** operar a plataforma com segurança.

#### Critérios de aceite

- Deve haver runbooks para:
  - deploy;
  - rollback;
  - backup/restore;
  - reindexação;
  - falha de ingestão;
  - indisponibilidade de IA;
  - vazamento de dados ou incidente.
- A IA deve sugerir atualizações após incidentes.
- Todo runbook deve ter dono e data de revisão.

---

# 9. Backlog consolidado por fase

| Fase | ID | História | Prioridade |
|---|---|---|---|
| Fase 0 | US-001 | Instalação local simplificada | Alta |
| Fase 0 | US-002 | Configuração por ambiente | Alta |
| Fase 0 | US-003 | Provisionamento IaC | Alta |
| Fase 0 | US-004 | Observabilidade básica | Alta |
| Fase 0 | US-005 | Boot de documentação automática | Alta |
| Fase 1 | US-101 | Cadastro de fontes | Alta |
| Fase 1 | US-102 | Coleta automática | Alta |
| Fase 1 | US-103 | Extração estruturada | Alta |
| Fase 1 | US-104 | Classificação automática | Alta |
| Fase 1 | US-105 | Versionamento de normas | Alta |
| Fase 1 | US-106 | Curadoria humana | Alta |
| Fase 1 | US-107 | Auditoria de ingestão | Alta |
| Fase 2 | US-201 | Catálogo de produtos | Alta |
| Fase 2 | US-202 | Catálogo de modalidades | Alta |
| Fase 2 | US-203 | Catálogo de carteiras | Média |
| Fase 2 | US-204 | Catálogo de convênios | Alta |
| Fase 2 | US-205 | Catálogo de capacidades | Alta |
| Fase 2 | US-206 | Catálogo de bounded contexts | Alta |
| Fase 2 | US-207 | Ontologia mínima | Alta |
| Fase 3 | US-301 | Indexação vetorial | Alta |
| Fase 3 | US-302 | Grafo de conhecimento | Alta |
| Fase 3 | US-303 | Resposta com citação | Alta |
| Fase 3 | US-304 | Consulta de impacto | Alta |
| Fase 3 | US-305 | RAG com controle de acesso | Alta |
| Fase 4 | US-401 | Catálogo de serviços | Alta |
| Fase 4 | US-402 | Importação OpenAPI | Média |
| Fase 4 | US-403 | Importação repositórios | Média |
| Fase 4 | US-404 | Matriz Base vs Construído | Alta |
| Fase 4 | US-405 | Rastreabilidade regra-código | Alta |
| Fase 5 | US-501 | Assistente conversacional | Alta |
| Fase 5 | US-502 | Agente arquiteto | Alta |
| Fase 5 | US-503 | Agente product manager | Média |
| Fase 5 | US-504 | Agente regulatório | Alta |
| Fase 5 | US-505 | Agente QA | Média |
| Fase 5 | US-506 | Agente de documentação | Alta |
| Fase 5 | US-507 | Prompt registry | Alta |
| Fase 6 | US-601 | Radar de tendências | Média |
| Fase 6 | US-602 | Análise de gap | Alta |
| Fase 6 | US-603 | Simulador de novo produto | Média |
| Fase 6 | US-604 | Recomendação de reuso | Média |
| Fase 7 | US-701 | Autenticação e autorização | Alta |
| Fase 7 | US-702 | Backup e restore | Alta |
| Fase 7 | US-703 | Qualidade de dados | Alta |
| Fase 7 | US-704 | Avaliação de IA | Alta |
| Fase 7 | US-705 | Runbooks | Alta |

---

# 10. Requisitos Não Funcionais

## 10.1 Usabilidade

- Interface simples para curadoria e consulta.
- Busca com linguagem natural.
- Dashboard executivo com gaps e riscos.
- Exportação de relatórios em Markdown, PDF, CSV e JSON.

## 10.2 Performance

- Busca semântica com resposta em até 3 segundos para consultas simples.
- Consultas de grafo comuns em até 5 segundos.
- Ingestão assíncrona para documentos grandes.
- Suporte inicial a pelo menos 10 mil documentos normalizados.

## 10.3 Confiabilidade

- Jobs de ingestão idempotentes.
- Retentativas com backoff exponencial.
- Estado de processamento persistente.
- Backup automático.
- Restauração testada.

## 10.4 Segurança

- Autenticação OIDC/OAuth2.
- Autorização por papéis e recursos.
- Criptografia em trânsito com TLS.
- Criptografia em repouso quando aplicável.
- Segredos fora do código.
- Logs sem exposição de dados sensíveis.
- Auditoria de acesso e alteração.

## 10.5 Privacidade e LGPD

- Controle de acesso a documentos sensíveis.
- Retenção configurável por tipo documental.
- Minimização de dados pessoais quando possível.
- Registro de consentimento quando aplicável.
- Capacidade de exportar ou anonimizar dados mediante solicitação aprovada.

## 10.6 Portabilidade

- Deve rodar localmente com Docker Compose.
- Deve permitir migração para Kubernetes.
- Deve evitar lock-in excessivo.
- Deve permitir troca de provedor de IA por configuração.
- Deve permitir backup e restore completo.

## 10.7 Observabilidade

- Logs estruturados.
- Métricas de API, ingestão, IA e banco.
- Traces distribuídos.
- Alertas para falhas de ingestão, latência e erro de IA.
- Dashboard operacional.

## 10.8 Qualidade de IA

- Respostas devem citar fontes.
- Deve haver avaliação contínua de prompts.
- Deve haver limite de confiança.
- Deve haver fallback quando não houver informação suficiente.
- Deve haver revisão humana para conteúdo regulatório crítico.

---

# 11. Critérios de Aceite Globais

Toda funcionalidade entregue deve:

1. possuir documentação atualizada;
2. possuir testes automatizados;
3. estar registrada no catálogo de componentes;
4. possuir trilha de auditoria quando crítica;
5. respeitar controle de acesso;
6. ser instalável ou migrável pelos scripts oficiais;
7. gerar evidência de execução;
8. não introduzir segredo em código;
9. possuir observabilidade mínima;
10. possuir rollback ou plano de reversão.

---

# 12. Definition of Ready

Uma user story está pronta para desenvolvimento quando:

- objetivo claro;
- critérios de aceite definidos;
- dependências identificadas;
- impacto em dados identificado;
- necessidade de UI definida;
- riscos de segurança avaliados;
- fonte de conhecimento associada, quando aplicável;
- testes mínimos definidos;
- documentação esperada especificada.

---

# 13. Definition of Done

Uma user story está concluída quando:

- código implementado;
- testes automatizados passando;
- documentação gerada/atualizada;
- migrações de banco aplicáveis funcionando;
- feature funcionando em ambiente local;
- observabilidade implementada;
- auditoria implementada quando aplicável;
- curadoria humana aprovada quando aplicável;
- métricas de qualidade de IA registradas quando aplicável;
- rollback testado ou documentado;
- PR revisado e aprovado.

---

# 14. Métricas de Sucesso

## 14.1 Produto

- percentual de normas críticas catalogadas;
- percentual de produtos com mapa de capacidades completo;
- número de consultas úteis realizadas;
- satisfação dos usuários internos;
- redução de tempo para análise de impacto regulatório.

## 14.2 Engenharia

- percentual de serviços catalogados;
- percentual de APIs documentadas automaticamente;
- cobertura de testes por regra crítica;
- tempo médio de deploy;
- tempo de recuperação de ambiente.

## 14.3 IA

- percentual de respostas com citação válida;
- taxa de alucinação em perguntas douradas;
- precisão em testes de rastreabilidade;
- aprovação humana das análises;
- tempo médio para geração de backlog inicial.

## 14.4 Governança

- percentual de documentos aprovados por curadoria;
- número de regras críticas sem teste;
- número de normas sem responsável;
- tempo médio para atualizar base após nova norma;
- quantidade de evidências auditáveis geradas.

---

# 15. Roadmap sugerido

## MVP — 8 a 12 semanas

### Objetivo

Provar valor com consignado INSS.

### Entregas

- ambiente local Docker Compose;
- ingestão de normas e documentos;
- catálogo de produtos e modalidades;
- catálogo de capacidades e bounded contexts;
- busca semântica com citação;
- grafo mínimo;
- matriz Base vs Construído simples;
- assistente IA básico;
- documentação automática inicial.

### Critério de sucesso

O usuário deve conseguir perguntar:

```text
Quais contextos são necessários para implementar empréstimo consignado INSS?
```

E receber:

- lista de contextos;
- entidades;
- regras;
- integrações;
- normas relacionadas;
- lacunas iniciais.

---

## Fase 2 — 12 a 16 semanas

### Objetivo

Conectar conhecimento ao inventário real de sistemas.

### Entregas

- importação de OpenAPI;
- catálogo de serviços;
- rastreabilidade regra → serviço → teste;
- gap analysis mais robusto;
- agentes de arquitetura e QA;
- dashboard executivo.

---

## Fase 3 — 16 a 24 semanas

### Objetivo

Operação produtiva e inovação.

### Entregas

- deploy Kubernetes;
- segurança e RBAC;
- avaliação de IA;
- radar de tendências;
- simulador de novo produto;
- integração com ferramentas de backlog;
- runbooks produtivos.

---

# 16. Diretrizes para desenvolvimento com Antigravity + IA

O ambiente Antigravity deve atuar como uma fábrica orientada por agentes.

## 16.1 Papéis dos agentes

| Agente | Responsabilidade |
|---|---|
| Planner Agent | Quebra épicos em tarefas técnicas |
| Architect Agent | Sugere bounded contexts, serviços e APIs |
| Coder Agent | Gera código, testes e migrações |
| Reviewer Agent | Revisa padrões, segurança e arquitetura |
| QA Agent | Gera cenários e valida critérios de aceite |
| Doc Agent | Atualiza documentação e ADRs |
| Data Agent | Mantém schema, seed e migrações |
| DevOps Agent | Mantém Docker, CI/CD, IaC e deploy |
| Compliance Agent | Verifica rastreabilidade regulatória |

---

## 16.2 Fluxo de trabalho sugerido

```text
1. Product Manager cria épico ou pergunta de negócio.
2. Planner Agent consulta knowledge graph.
3. Architect Agent gera proposta de contexto e serviços.
4. Coder Agent implementa tarefas.
5. QA Agent cria testes baseados em critérios.
6. Reviewer Agent revisa código e riscos.
7. Doc Agent atualiza documentação.
8. DevOps Agent valida deploy local.
9. Compliance Agent registra evidências.
10. Humano aprova entrega.
```

---

## 16.3 Regras para agentes IA

- Agentes não devem alterar produção sem aprovação humana.
- Agentes devem sempre consultar a base antes de gerar respostas críticas.
- Agentes devem registrar decisões relevantes.
- Agentes devem indicar incerteza quando não houver fonte.
- Agentes devem sugerir testes para toda regra crítica.
- Agentes devem gerar documentação junto com código.
- Agentes devem respeitar permissões e segredos.

---

# 17. Modelo de dados simplificado

## 17.1 Entidades principais

```text
Source
Document
DocumentVersion
Regulation
BusinessRule
Product
Modality
Portfolio
Agreement
Capability
BoundedContext
Service
API
Event
Repository
Test
Control
Evidence
Gap
Trend
PromptVersion
AuditEvent
```

---

## 17.2 Relações principais

```text
Regulation -> BusinessRule
BusinessRule -> Capability
Capability -> BoundedContext
BoundedContext -> Service
Service -> API
API -> Test
BusinessRule -> Test
Product -> Capability
Product -> Regulation
Product -> Modality
Portfolio -> Product
Agreement -> Portfolio
Service -> Repository
Gap -> Capability
Gap -> Service
Trend -> Product
Trend -> Capability
AuditEvent -> any entity
```

---

# 18. Exemplo de aplicação ao domínio consignado

## Pergunta esperada

```text
Quais contextos delimitados existem no domínio de consignado?
```

## Resposta esperada da plataforma

A plataforma deve retornar algo como:

```text
1. Elegibilidade
2. Simulação e Pricing
3. Proposta
4. Assinatura e Formalização
5. Margem Consignável
6. Averbação
7. Registro de Contrato
8. Liberação de Crédito
9. Gestão de Contrato
10. Cobrança em Folha
11. Portabilidade e Quitação
12. Contabilidade
13. Risco e Provisão
14. Reporte Regulatório
15. Compliance, Auditoria e LGPD
```

Para cada contexto, deve retornar:

- entidades;
- regras;
- normas;
- APIs;
- eventos;
- serviços;
- testes;
- gaps.

---

# 19. Exemplo de matriz de rastreabilidade para consignado

| Capacidade | Regra | Contexto | Serviço | Status | Teste | Evidência |
|---|---|---|---|---|---|---|
| Validar margem | Margem máxima vigente | Margem Consignável | margin-service | Implementado | MarginValidationSpec | link |
| Averbar contrato | Averbação obrigatória | Averbação | averbation-service | Parcial | AverbationTimeoutSpec | link |
| Registrar contrato | Registro em entidade autorizada | Registro | contract-registry-service | Ausente | nenhum | gap |
| Reportar SCR | Envio mensal | Regulatório | scr-reporting | Implementado | ScrSchemaTest | link |
| Contabilizar liberação | Evento COSIF | Contabilidade | accounting-service | Parcial | AccountingEventSpec | link |

---

# 20. Riscos e mitigações

| Risco | Impacto | Mitigação |
|---|---|---|
| Normas desatualizadas | Alto | Versionamento, curadoria humana e monitoramento de fontes oficiais |
| Extração ruim de PDFs | Médio | OCR, revisão humana, marcação de baixa confiança |
| Alucinação da IA | Alto | RAG com citação, testes de fidelidade, revisão humana |
| Falta de adesão dos times | Alto | UX simples, integração com fluxo existente, valor rápido |
| Complexidade excessiva | Alto | MVP focado em consignado INSS |
| Segurança de dados sensíveis | Alto | RBAC, auditoria, criptografia, segredos gerenciados |
| Dependência de provedor de IA | Médio | Abstração de provedor e fallback local/configurável |
| Dificuldade de migrar para produção | Médio | Docker Compose, IaC, Helm, runbooks e backups |
| Baixa qualidade de inventário | Médio | Importação automática de OpenAPI, Git e catálogos existentes |
| Mudança regulatória frequente | Alto | Pipeline de monitoramento e análise de impacto |

---

# 21. Plano de migração para produção

## 21.1 Estratégia

1. Validar ambiente local com Docker Compose.
2. Criar imagens Docker versionadas.
3. Provisionar infraestrutura com Terraform.
4. Instalar aplicação com Helm.
5. Configurar segredos e autenticação.
6. Configurar observabilidade.
7. Executar migrações de banco.
8. Restaurar backup de homologação para validar.
9. Executar smoke tests.
10. Liberar acesso controlado.
11. Monitorar por período de estabilização.
12. Documentar lições aprendidas.

---

## 21.2 Artefatos obrigatórios de deploy

```text
docker-compose.yml
Dockerfile
Makefile
.env.example
values-local.yaml
values-dev.yaml
values-prod.yaml
terraform/
helm/
docs/runbook-deploy.md
docs/runbook-restore.md
docs/runbook-incident.md
```

---

# 22. Critérios mínimos para MVP aprovado

O MVP deve permitir:

1. subir ambiente local com `make up`;
2. ingerir pelo menos um conjunto de normas de consignado;
3. catalogar produto consignado INSS;
4. cadastrar capacidades e bounded contexts;
5. buscar normas com citação;
6. perguntar à IA quais contextos compõem consignado;
7. visualizar matriz Base vs Construído simples;
8. gerar documentação inicial automaticamente;
9. executar testes automatizados;
10. exportar relatório em Markdown.

---

# 23. Próximos passos recomendados

1. aprovar este PRD;
2. iniciar Fase 0 com setup do repositório;
3. definir arquitetura inicial e ADRs;
4. criar ontologia mínima;
5. selecionar documentos de consignado para MVP;
6. criar catálogos iniciais;
7. implementar pipeline de ingestão;
8. implementar busca com citação;
9. validar com usuários de negócio;
10. evoluir para inventário de sistemas e agentes IA.

---

# 24. Aprovação

| Papel | Nome | Data | Aprovação |
|---|---|---|---|
| Product Owner |  |  |  |
| Arquitetura |  |  |  |
| Engenharia |  |  |  |
| Compliance |  |  |  |
| Segurança |  |  |  |
| Operação |  |  |  |

---

## Anexo A — Prompt mestre sugerido para o Antigravity

```text
Você é um agente de construção de software para uma plataforma de conhecimento financeiro.
Sua missão é implementar funcionalidades seguindo este PRD.

Regras obrigatórias:
1. Sempre consulte a ontologia e os catálogos existentes antes de criar novas entidades.
2. Sempre gere documentação junto com código.
3. Sempre proponha testes para critérios de aceite.
4. Sempre registre decisões relevantes como ADR.
5. Sempre utilize configuração por ambiente e nunca fixe segredos.
6. Sempre priorize portabilidade: Docker Compose local e Helm/Terraform para produção.
7. Sempre que criar uma regra de negócio, associe-a a produto, capacidade, contexto e evidência.
8. Sempre que uma resposta depender de norma, cite a fonte.
9. Se não houver informação suficiente, declare incerteza e sugira curadoria humana.
10. Nunca altere produção sem aprovação humana.
```

---

## Anexo B — Estrutura de repositório sugerida

```text
/finknowledge-antigravity
├── apps/
│   ├── api/
│   ├── web-admin/
│   ├── chat-ui/
│   └── workers/
├── agents/
│   ├── architect-agent/
│   ├── pm-agent/
│   ├── qa-agent/
│   ├── compliance-agent/
│   └── doc-agent/
├── pipelines/
│   ├── ingestion/
│   ├── normalization/
│   ├── classification/
│   └── evaluation/
├── infra/
│   ├── docker-compose.yml
│   ├── helm/
│   └── terraform/
├── db/
│   ├── migrations/
│   └── seeds/
├── knowledge/
│   ├── ontology/
│   ├── taxonomy/
│   └── prompts/
├── docs/
│   ├── adr/
│   ├── runbooks/
│   ├── glossary/
│   └── reports/
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── e2e/
│   └── ai-evals/
├── Makefile
├── README.md
└── .env.example
```

---

## Anexo C — Comandos desejados

```bash
make setup
make up
make down
make seed
make migrate
make test
make ai-eval
make docs
make backup
make restore
make deploy-dev
make deploy-prod
```

---

## Anexo D — Exemplo de épico inicial

### Épico: Plataforma auto-documentada de conhecimento financeiro

**Descrição:**  
Criar base técnica e conceitual para ingestão, catalogação, rastreabilidade e análise de conhecimento financeiro com IA.

**Critérios de saída:**
- ambiente local instalável;
- ingestão documental funcionando;
- catálogo de produtos e capacidades funcionando;
- busca semântica com citação funcionando;
- matriz Base vs Construído disponível;
- documentação automática gerada;
- testes automatizados passando.

**Histórias relacionadas:**
- US-001
- US-002
- US-004
- US-101
- US-102
- US-103
- US-201
- US-205
- US-301
- US-303
- US-404
- US-506

---

# Conclusão

Este PRD define uma plataforma incremental, auto-documentada e portável para transformar conhecimento financeiro, regulatório e arquitetural em vantagem operacional para a fábrica de software.

A chave do projeto é começar pequeno, mas com base sólida:

1. **infraestrutura fácil de instalar;**
2. **ingestão de conhecimento;**
3. **ontologia financeira;**
4. **catálogos de produto e domínio;**
5. **grafo e busca semântica;**
6. **inventário de sistemas;**
7. **agentes de IA;**
8. **análise de gaps e tendências;**
9. **governança e produção.**
