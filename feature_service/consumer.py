from kafka import KafkaConsumer
from feature_service.redis_store import RedisStore
import json


class FeatureConsumer:
    def __init__(self):
        self.consumer = KafkaConsumer('transactions', bootstrap_servers = 'localhost:9092', value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            
            auto_offset_reset="earliest")

    def get_transaction(self):
        for message in self.consumer:   
            return message.value