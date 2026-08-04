from kafka import KafkaConsumer
import json
from inference_service.service import FraudDetectionService
from common.config import KAFKA_BOOTSTRAP_SERVERS
from inference_service.metrics_server import start_metrics_server


start_metrics_server()

fraud_detection_service = FraudDetectionService()

consumer = KafkaConsumer(
    "enriched_transaction_v2",
    bootstrap_servers = KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer =  lambda m : json.loads(m.decode("utf-8")),
    auto_offset_reset = "latest",
    group_id = "inference_service",
    
)

for message in consumer:
    transaction = message.value
    print("="*60)
    prediction = fraud_detection_service.process_transaction(transaction)
    

    


