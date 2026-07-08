from kafka import KafkaConsumer
from dataclasses import asdict
import json

consumer = KafkaConsumer('transactions', bootstrap_servers = 'localhost:9092', value_deserializer=lambda m: json.loads(m.decode("utf-8")),
group_id="feature-service",
auto_offset_reset="earliest")



for message in consumer:
        transaction = message.value
        print(
            f"""
        Transaction ID : {transaction['transaction_id']}
        Sender         : {transaction['sender_id']}
        Receiver       : {transaction['receiver_id']}
        Amount         : ₹{transaction['amount']}
        Merchant       : {transaction['merchant']}
        """
        )
