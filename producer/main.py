from producer.simulator import TransactionSimulator
from producer.producer import TransactionProducer
import time

simulator = TransactionSimulator()
producer = TransactionProducer()


while True:
    transaction = simulator.generate_transaction()

    producer.send(transaction)
    print(
            f"""
        Transaction ID : {transaction.transaction_id}
        Sender         : {transaction.sender_id}
        Receiver       : {transaction.receiver_id}
        Amount         : ₹{transaction.amount}
        Merchant       : {transaction.merchant}
        """
        )
    time.sleep(0.2)