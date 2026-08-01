from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from common.config import POSTGRES_HOST, POSTGRES_DB,


DATABASE_URL = (
    "postgresql://fraud_user:"
    "fraud_password@localhost:5432/fraud_db"
)


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind = engine
)