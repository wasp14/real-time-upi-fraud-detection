from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserProfile:
    user_id: str
    age: int
    occupation: str
    city: str
    state: str
    monthly_income: float
    average_transaction: float
    max_normal_transaction: float
    preferred_start_hour: int
    preferred_end_hour: int
    device_id: str
    device_type: str
    operating_system: str
    network_provider: str



@dataclass
class Transaction:
    transaction_id: str
    timestamp: datetime
    sender_id: str
    receiver_id: str
    amount: float
    merchant: str
    merchant_category: str
    city: str
    state: str
    device_id: str
    payment_mode: str
