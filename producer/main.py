from producer.simulator import TransactionSimulator
from producer.producer import TransactionProducer
import time

simulator = TransactionSimulator()
producer = TransactionProducer()


while True:
    transaction = simulator.generate_transaction()

    producer.send(transaction)
    print(transaction)
    time.sleep(0.2)