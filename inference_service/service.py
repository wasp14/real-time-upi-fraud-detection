from inference_service.predictor import FraudPredictor
from inference_service.alert_producer import AlertProducer
from common.models import EnrichedTransaction
from inference_service.schema import TransactionFeatures
from inference_service.metrics import (
    transactions_processed,
    fraud_predictions,
    normal_predictions,
    prediction_latency,
    alerts_published,
    fraud_probability
)
class FraudDetectionService:

    def __init__(self):
        self.predictor = FraudPredictor()
        self.alert_producer = AlertProducer()


    def process_transaction(self, transaction):
        transactions_processed.inc()
        transaction_features = {
            "amount_ratio" : transaction["amount_ratio"],
            "time_since_last_txn" :  transaction["time_since_last_txn"],
            "transaction_velocity" : transaction["txn_velocity"],
            "device_changed" :  transaction["device_changed"],
            "city_changed": transaction["city_changed"],
            "merchant_changed" : transaction["merchant_changed"]
       }  
        with prediction_latency.time():
            prediction = self.predictor.predict(transaction_features)

        print(f"Transaction : {transaction['transaction_id']}")
        print(f"Prediction  : {prediction['prediction']}")
        print(f"Top Features: {prediction["top_features"]}")

        fraud_probability.observe(prediction["probability"])


        if prediction["prediction"] == "Fraud":
            fraud_predictions.inc()
            alert = {
                "transaction_id": transaction["transaction_id"],
                "sender_id": transaction["sender_id"],
                "receiver_id": transaction["receiver_id"],
                "probability": prediction["probability"],
                "top_features": prediction["top_features"]
            }

            self.alert_producer.publish_alert(alert)
            alerts_published.inc()
        else:
            normal_predictions.inc()    
        return prediction


