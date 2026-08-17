from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Enum, JSON, Boolean, Float
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
import enum
import uuid

Base = declarative_base()

class SourceType(str, enum.Enum):
    BACEN = "BACEN"
    CMN = "CMN"
    PLANALTO = "PLANALTO"
    INTERNAL = "INTERNAL"
    MANUAL = "MANUAL"
    API = "API"

class SourceStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

class DocumentStatus(str, enum.Enum):
    PENDING_EXTRACTION = "PENDING_EXTRACTION"
    PENDING_CLASSIFICATION = "PENDING_CLASSIFICATION"
    PENDING_REVIEW = "PENDING_REVIEW"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    ERROR = "ERROR"

def generate_uuid():
    return str(uuid.uuid4())

class Source(Base):
    __tablename__ = "sources"

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    source_type = Column(Enum(SourceType), nullable=False)
    entity = Column(String, nullable=True)
    status = Column(Enum(SourceStatus), default=SourceStatus.ACTIVE)
    last_collected_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    documents = relationship("Document", back_populates="source")

class Document(Base):
    __tablename__ = "documents"

    id = Column(String, primary_key=True, default=generate_uuid)
    source_id = Column(String, ForeignKey("sources.id"), nullable=False)
    title = Column(String, nullable=True)
    original_url = Column(String, nullable=True)
    hash = Column(String, nullable=False, unique=True)
    content_raw_path = Column(String, nullable=True) # S3/MinIO path
    extracted_text = Column(Text, nullable=True)
    status = Column(Enum(DocumentStatus), default=DocumentStatus.PENDING_EXTRACTION)
    
    # Metadata suggested by AI
    metadata_json = Column(JSON, nullable=True)
    
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    source = relationship("Source", back_populates="documents")
    versions = relationship("DocumentVersion", back_populates="document")

class DocumentVersion(Base):
    __tablename__ = "document_versions"

    id = Column(String, primary_key=True, default=generate_uuid)
    document_id = Column(String, ForeignKey("documents.id"), nullable=False)
    version = Column(String, nullable=False)
    hash = Column(String, nullable=False)
    extracted_text = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())

    document = relationship("Document", back_populates="versions")

class AuditEvent(Base):
    __tablename__ = "audit_events"

    id = Column(String, primary_key=True, default=generate_uuid)
    action = Column(String, nullable=False)
    entity_id = Column(String, nullable=False)
    entity_type = Column(String, nullable=False)
    details = Column(JSON, nullable=True)
    user_id = Column(String, nullable=True) # e.g. 'system' or UUID
    timestamp = Column(DateTime, default=func.now())

# ==========================================
# FASE 2: TAXONOMIA, ONTOLOGIA E CATÁLOGOS
# ==========================================

class StatusEnum(str, enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    MIGRATING = "MIGRATING"

class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, default=generate_uuid)
    code = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    family = Column(String, nullable=False)
    segment = Column(String, nullable=False)
    status = Column(Enum(StatusEnum), default=StatusEnum.ACTIVE)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    modalities = relationship("Modality", back_populates="product")
    portfolios = relationship("Portfolio", back_populates="product")

class Modality(Base):
    __tablename__ = "modalities"

    id = Column(String, primary_key=True, default=generate_uuid)
    product_id = Column(String, ForeignKey("products.id"), nullable=False)
    code = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    discount_type = Column(String, nullable=True)
    margin_controller = Column(String, nullable=True)
    max_term = Column(String, nullable=True)
    requires_averbation = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    product = relationship("Product", back_populates="modalities")
    portfolios = relationship("Portfolio", back_populates="modality")

class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(String, primary_key=True, default=generate_uuid)
    product_id = Column(String, ForeignKey("products.id"), nullable=False)
    modality_id = Column(String, ForeignKey("modalities.id"), nullable=True)
    code = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    risk_policy = Column(String, nullable=True)
    accounting_policy = Column(String, nullable=True)
    status = Column(Enum(StatusEnum), default=StatusEnum.ACTIVE)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    product = relationship("Product", back_populates="portfolios")
    modality = relationship("Modality", back_populates="portfolios")

class Agreement(Base):
    __tablename__ = "agreements"

    id = Column(String, primary_key=True, default=generate_uuid)
    code = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    agreement_type = Column(String, nullable=False)
    integration_channel = Column(String, nullable=True)
    status = Column(Enum(StatusEnum), default=StatusEnum.ACTIVE)
    # JSONB for specific margin rules as discussed
    specific_rules = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Capability(Base):
    __tablename__ = "capabilities"

    id = Column(String, primary_key=True, default=generate_uuid)
    parent_id = Column(String, ForeignKey("capabilities.id"), nullable=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    domain = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    sub_capabilities = relationship("Capability")

class BoundedContext(Base):
    __tablename__ = "bounded_contexts"

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    domain = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class BusinessRule(Base):
    __tablename__ = "business_rules"

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    rule_type = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

# ==========================================
# FASE 4: INVENTÁRIO DE SISTEMAS E RASTREABILIDADE
# ==========================================

class Repository(Base):
    __tablename__ = "repositories"

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    provider = Column(String, nullable=True) # Github, Gitlab
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Service(Base):
    __tablename__ = "services"

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, unique=True, nullable=False)
    domain = Column(String, nullable=False)
    repository_id = Column(String, ForeignKey("repositories.id"), nullable=True)
    description = Column(Text, nullable=True)
    status = Column(Enum(StatusEnum), default=StatusEnum.ACTIVE)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    repository = relationship("Repository")
    endpoints = relationship("APIEndpoint", back_populates="service")

class APIEndpoint(Base):
    __tablename__ = "api_endpoints"

    id = Column(String, primary_key=True, default=generate_uuid)
    service_id = Column(String, ForeignKey("services.id"), nullable=False)
    method = Column(String, nullable=False) # GET, POST
    path = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())

    service = relationship("Service", back_populates="endpoints")

class Event(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    domain = Column(String, nullable=False)
    producer_service_id = Column(String, ForeignKey("services.id"), nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())

# ==========================================
# FASE 5: AGENTES E WORKFLOWS
# ==========================================

class PromptRegistry(Base):
    __tablename__ = "prompt_registry"

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    version = Column(String, nullable=False)
    objective = Column(Text, nullable=True)
    model_name = Column(String, nullable=False)
    system_prompt = Column(Text, nullable=False)
    parameters = Column(JSON, nullable=True)
    owner = Column(String, nullable=True)
    status = Column(Enum(StatusEnum), default=StatusEnum.ACTIVE)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

# ==========================================
# FASE 6: INOVAÇÃO, GAPS E SIMULAÇÕES
# ==========================================

class Trend(Base):
    __tablename__ = "trends"

    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    source_url = Column(String, nullable=True)
    category = Column(String, nullable=False) # e.g. technology, regulation, product
    relevance_score = Column(String, nullable=True)
    affected_domains = Column(JSON, nullable=True)
    status = Column(Enum(StatusEnum), default=StatusEnum.ACTIVE)
    created_at = Column(DateTime, default=func.now())

class GapAnalysis(Base):
    __tablename__ = "gap_analyses"

    id = Column(String, primary_key=True, default=generate_uuid)
    product_id = Column(String, ForeignKey("products.id"), nullable=False)
    gaps = Column(JSON, nullable=False) # functional, technical, regulatory
    priority_score = Column(String, nullable=True)
    suggested_epics = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=func.now())

class Simulation(Base):
    __tablename__ = "simulations"

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    parameters = Column(JSON, nullable=False) # family, modality, etc.
    results = Column(JSON, nullable=True) # capabilities, norms, backlog
    created_at = Column(DateTime, default=func.now())

# ==========================================
# FASE 7: GOVERNANÇA, SEGURANÇA E QUALIDADE
# ==========================================

class Role(Base):
    __tablename__ = "roles"
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=generate_uuid)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=True)
    is_active = Column(Boolean, default=True)

class UserRole(Base):
    __tablename__ = "user_roles"
    user_id = Column(String, ForeignKey("users.id"), primary_key=True)
    role_id = Column(String, ForeignKey("roles.id"), primary_key=True)

class DataQualityReport(Base):
    __tablename__ = "data_quality_reports"
    id = Column(String, primary_key=True, default=generate_uuid)
    entity_type = Column(String, nullable=False) # e.g. "product", "trend"
    entity_id = Column(String, nullable=True)
    quality_score = Column(Float, nullable=False)
    issues = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=func.now())

class AIEvaluation(Base):
    __tablename__ = "ai_evaluations"
    id = Column(String, primary_key=True, default=generate_uuid)
    agent_name = Column(String, nullable=False)
    prompt_id = Column(String, ForeignKey("prompt_registry.id"), nullable=True)
    evaluation_score = Column(Float, nullable=False)
    metrics = Column(JSON, nullable=True) # toxicity, coherence, groundedness
    feedback = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())
