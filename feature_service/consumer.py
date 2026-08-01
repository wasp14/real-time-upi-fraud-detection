from kafka import KafkaConsumer
from feature_service.redis_store import RedisStore
import json
from common.config import KAFKA_BOOTSTRAP_SERVERS
from common.models import Transaction


class FeatureConsumer:
    def __init__(self):
        self.consumer = KafkaConsumer('transactions_v4', bootstrap_servers = KAFKA_BOOTSTRAP_SERVERS, value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            group_id="feature-service-dev",
            auto_offset_reset="latest")

    def get_transaction(self):
        for message in self.consumer:   
            print("Message is : ", message.value)
            return Transaction(**message.value)