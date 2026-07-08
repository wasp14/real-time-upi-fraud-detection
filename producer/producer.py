from kafka import KafkaProducer
from kafka.errors import KafkaError
from dataclasses import asdict
import json



class TransactionProducer:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers="localhost:9092",  key_serializer=lambda k: k.encode("utf-8"),   value_serializer= lambda v: json.dumps(v).encode("utf-8"))


    def send(self, transaction):
            self.producer.send("transactions",key = transaction.sender_id, value = asdict(transaction) ) 
            self.producer.flush()
            
            
    
        


