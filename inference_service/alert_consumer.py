from kafka import KafkaConsumer
from common.config import KAFKA_BOOTSTRAP_SERVERS
import json

while True:
    try:
        consumer = KafkaConsumer(
            "fraud_alerts",
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            auto_offset_reset="latest",
            group_id="alert-service"
        )
        break
    except Exception:
        print("Waiting for Kafka..")
        time.sleep(5) 

print("Listening for fraud alerts...")
print(60*"=")
for message in consumer:
    print(message.value)