from fastapi import FastAPI

from inference_service.predictor import FraudPredictor
from inference_service.schema import (
    TransactionFeatures,
    PredictionResponse
)

predictor = FraudPredictor()

app = FastAPI(
    title = "Fraud Detection"

)

predictor = FraudPredictor()

@app.get("/health")
def health():
    return {
        "status" : "healthy"
    }

@app.post(
    "/predict",
    response_model = PredictionResponse
)
def predict(
    transaction: TransactionFeatures
):

    prediction  = predictor.predict(transaction.model_dump())

    return prediction
