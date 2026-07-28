from dataclasses import dataclass
from datetime import datetime
from enum import Enum

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
    transaction_std_dev: float
    preferred_start_hour: int
    preferred_end_hour: int
    device_id: str
    device_type: str
    operating_system: str
    network_provider: str
    preferred_merchants: list[tuple[str, str]]

@dataclass
class Merchant:
    name: str
    category: str    


class SimulationMode(Enum):
    NORMAL = "normal"
    TRAINING = "training"
    VELOCITY_TEST = "velocity_test"
    ACCOUNT_TAKEOVER_TEST = "account_takeover_test"
    MERCHANT_SCAM_TEST = "merchant_scam_test"


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
    is_fraud : bool


@dataclass
class UserProfileForFS:
    avg_amount: float
    transaction_count: int
    last_transaction_time: str
    last_device: str
    last_city: str
    last_merchant: str


    @classmethod
    def from_redis(cls, data):
        return cls(
            
            avg_amount=float(data["avg_amount"]),
            transaction_count=int(data["transaction_count"]),
            last_transaction_time=data["last_transaction_time"],
            last_device=data["last_device"],
            last_city=data["last_city"],
            last_merchant=data["last_merchant"]
        )


@dataclass
class EnrichedTransaction:
    transaction_id : str
    sender_id  : str
    receiver_id  : str
    amount : float
    amount_ratio : int
    time_since_last_txn :str
    device_changed : bool  
    city_changed : bool
    merchant_changed : bool
    txn_velocity : int
    is_fraud : bool

