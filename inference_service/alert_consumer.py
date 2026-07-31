from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "fraud_alerts",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset="latest",
    group_id="alert-service"
)

print("Listening for fraud alerts...")

for message in consumer:
    print(message.value)