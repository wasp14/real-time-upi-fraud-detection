import json
from kafka import KafkaProducer

class AlertProducer:
    
    def __init__(self):

        self.producer = KafkaProducer(
            bootstrap_servers ="localhost:9092",
            value_serializer =lambda v: json.dumps(v).encode("utf-8")
        )

    def publish_alert(self, alert):
        self.producer.send(
            "fraud_alerts",
            value = alert
        )

        self.producer.flush()