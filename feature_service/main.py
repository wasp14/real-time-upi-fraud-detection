from feature_service.consumer import FeatureConsumer
from feature_service.features import Features


consumer = FeatureConsumer()


while True:
    print("Inside the while loop")
    transaction = consumer.get_transaction()
    features = Features(transaction)
    print(
            f"""
        Transaction ID : {transaction['transaction_id']}
        Sender         : {transaction['sender_id']}
        Receiver       : {transaction['receiver_id']}
        Amount         : ₹{transaction['amount']}
        Merchant       : {transaction['merchant']}
        """
        )