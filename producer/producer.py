from kafka import KafkaProducer
from kafka.errors import KafkaError
from dataclasses import asdict
import time
import random
import json
from common.config import KAFKA_BOOTSTRAP_SERVERS


class TransactionProducer:
    def __init__(self):
        print("KAFKA_BOOTSTRAP_SERVERS : ",KAFKA_BOOTSTRAP_SERVERS)
        while True:
            try:
                self.producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,  key_serializer=lambda k: k.encode("utf-8"),   value_serializer= lambda v: json.dumps(v).encode("utf-8"))
                break
            except Exception:
                print("Waiting for Kafka..")
                time.sleep(5)    

    def send(self, transaction):
            print("KAFKA_BOOTSTRAP_SERVERS : ",KAFKA_BOOTSTRAP_SERVERS)
            self.producer.send("transactions_v4",key = transaction.sender_id, value = asdict(transaction) ) 
            self.producer.flush()
            time.sleep(0.2)
            
            
            
    
        


