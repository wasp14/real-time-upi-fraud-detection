from feature_service.consumer import FeatureConsumer
from feature_service.features import Features
from common.models import Transaction
from feature_service.producer import EnrichedTransactionProducer
from common.models import EnrichedTransaction

consumer = FeatureConsumer()
enriched_transaction_producer = EnrichedTransactionProducer()

while True:
    print("Inside the while loop")
    transaction = consumer.get_transaction()
    
    feature_values = Features(transaction)
    enriched_transaction = feature_values.compute_features()
    enriched_transaction_producer.send(enriched_transaction)


    print(
            f"""
        Transaction ID : {transaction.transaction_id}
        Amount Ratio         : {enriched_transaction.amount_ratio}
        Time Diff       : {enriched_transaction.time_since_last_txn}
        Merchant_Changed : {enriched_transaction.merchant_changed}
        Device_Changed : {enriched_transaction.device_changed}
        Amount         : ₹{enriched_transaction.amount}
        Merchant_changed       : {enriched_transaction.merchant_changed}
        Txn_Velocity : {enriched_transaction.txn_velocity}
        """
        )