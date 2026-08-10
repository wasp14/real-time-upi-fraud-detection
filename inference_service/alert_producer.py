import json
import time
from kafka import KafkaProducer
from common.config import KAFKA_BOOTSTRAP_SERVERS

class AlertProducer:
    
    def __init__(self):

        while True:
            try:
                self.producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,  key_serializer=lambda k: k.encode("utf-8"),   value_serializer= lambda v: json.dumps(v).encode("utf-8"))
                break
            except Exception:
                print("Waiting for Kafka..")
                time.sleep(5) 

    def publish_alert(self, alert):
        self.producer.send(
            "fraud_alerts",
            key = alert["transaction_id"],
            value = alert
        )

        self.producer.flush()