from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = (
    "postgresql://fraud_user:"
    "fraud_password@localhost:5432/fraud_db"
)


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine
)