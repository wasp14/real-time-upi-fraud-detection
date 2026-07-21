from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Float, Integer, Boolean, Numeric


Base = declarative_base()


class EnrichedTransactionDB(Base):

    __tablename__ = "transactions"


    id = Column(Integer, primary_key=True, autoincrement=True)
    
    transaction_id = Column(String, unique=True, nullable=False)

    sender_id = Column(String)

    receiver_id = Column(String)

    amount = Column(Float)

    amount_ratio = Column(Float)

    time_since_last_txn = Numeric(10, 2)

    transaction_velocity = Column(Integer)

    device_changed = Column(Boolean)

    city_changed = Column(Boolean)

    merchant_changed = Column(Boolean)

    is_fraud = Column(Boolean)