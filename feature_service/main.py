from feature_service.consumer import FeatureConsumer
from feature_service.features import Features
from common.models import Transaction

consumer = FeatureConsumer()


while True:
    print("Inside the while loop")
    transaction = consumer.get_transaction()
    transaction = Transaction(transaction)
    features = Features(transaction)
    ratio = features.amount_ratio()
    time_diff = features.time_since_last_txn()
    features.update_profile()
    print(
            f"""
        Transaction ID : {transaction['transaction_id']}
        Amount Ratio         : {ratio}
        Time Diff       : {time_diff}
        Amount         : ₹{transaction['amount']}
        Merchant       : {transaction['merchant']}
        """
        )