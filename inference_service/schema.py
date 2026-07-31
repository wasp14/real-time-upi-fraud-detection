from pydantic import BaseModel

class TransactionFeatures(BaseModel):
    amount_ratio: float
    time_since_last_txn: float
    transaction_velocity: int
    device_changed: int
    city_changed: int
    merchant_changed: int


class FeatureContribution(BaseModel):
    feature: str
    impact: float


class PredictionResponse(BaseModel):
    prediction : str
    probability : float
    top_features: list[FeatureContribution]
