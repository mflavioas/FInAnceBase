import os
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
load_dotenv()

from db.models import Product, Modality, Agreement, Capability, StatusEnum

def get_url():
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5432")
    db = os.getenv("POSTGRES_DB", "finknowledge")
    return f"postgresql://{user}:{password}@{host}:{port}/{db}"

def run_seed():
    engine = create_engine(get_url())
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Seeding Ontologia Básica...")

    # Product
    prod_consig = session.query(Product).filter_by(code="CRED_CONSIG").first()
    if not prod_consig:
        prod_consig = Product(
            code="CRED_CONSIG",
            name="Crédito Consignado",
            family="Crédito PF",
            segment="Pessoa Física",
            description="Empréstimo com desconto em folha de pagamento."
        )
        session.add(prod_consig)
        session.commit()
    
    # Modality
    mod_inss = session.query(Modality).filter_by(code="CONSIG_INSS").first()
    if not mod_inss:
        mod_inss = Modality(
            product_id=prod_consig.id,
            code="CONSIG_INSS",
            name="Consignado INSS",
            discount_type="Benefício Previdenciário",
            margin_controller="Dataprev",
            max_term="84",
            requires_averbation="true"
        )
        session.add(mod_inss)
        session.commit()

    # Agreement
    agr_inss = session.query(Agreement).filter_by(code="AGR_INSS").first()
    if not agr_inss:
        agr_inss = Agreement(
            code="AGR_INSS",
            name="Convênio INSS",
            agreement_type="Federal",
            integration_channel="Dataprev API",
            specific_rules={"max_margin_pct": 35, "credit_card_margin_pct": 5, "benefit_card_margin_pct": 5}
        )
        session.add(agr_inss)
        session.commit()

    # Capabilities
    cap_orig = session.query(Capability).filter_by(name="Originação").first()
    if not cap_orig:
        cap_orig = Capability(name="Originação", domain="Crédito", description="Processo de venda e esteira de crédito.")
        session.add(cap_orig)
        session.commit()

        cap_sim = Capability(name="Simulação", domain="Crédito", parent_id=cap_orig.id)
        cap_marg = Capability(name="Reserva de Margem", domain="Crédito", parent_id=cap_orig.id)
        session.add_all([cap_sim, cap_marg])
        session.commit()

    print("Seed concluído com sucesso!")

if __name__ == "__main__":
    run_seed()
