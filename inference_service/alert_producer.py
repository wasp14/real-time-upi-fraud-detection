import json
from kafka import KafkaProducer
from common.config import KAFKA_BOOTSTRAP_SERVERS

class AlertProducer:
    
    def __init__(self):

        self.producer = KafkaProducer(
            bootstrap_servers = KAFKA_BOOTSTRAP_SERVERS,
            value_serializer = lambda v: json.dumps(v).encode("utf-8")
        )

    def publish_alert(self, alert):
        self.producer.send(
            "fraud_alerts",
            value = alert
        )

        self.producer.flush()