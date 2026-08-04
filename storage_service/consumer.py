from kafka import KafkaConsumer
from common.config import KAFKA_BOOTSTRAP_SERVERS
import json
from common.models import EnrichedTransaction
class StorageConsumer:
    def __init__(self):

        self.consumer = KafkaConsumer(
            "enriched_transaction_v2",
            bootstrap_servers =KAFKA_BOOTSTRAP_SERVERS,
            value_deserializer = lambda m: json.loads(
                m.decode("utf-8")
            ),
            group_id = "storage-service",
            auto_offset_reset = "latest"
        )


    def get_transaction(self):
        for message in self.consumer:
            return EnrichedTransaction(**message.value)