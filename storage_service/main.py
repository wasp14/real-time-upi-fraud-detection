from storage_service.consumer import StorageConsumer
from storage_service.database import SessionLocal
from storage_service.models import EnrichedTransactionDB


consumer = StorageConsumer()


while True:

    transaction = consumer.get_transaction()
    print("Inside the storage service transaction recieved")
    print(" Transaction is : ", transaction)
    db = SessionLocal()

    record = EnrichedTransactionDB(
        transaction_id=transaction.transaction_id,
        sender_id=transaction.sender_id,
        receiver_id=transaction.receiver_id,
        amount=transaction.amount,
        amount_ratio=transaction.amount_ratio,
        time_since_last_txn=transaction.time_since_last_txn,
        transaction_velocity=transaction.txn_velocity,
        device_changed=transaction.device_changed,
        city_changed=transaction.city_changed,
        merchant_changed=transaction.merchant_changed,
        is_fraud=transaction.is_fraud
    )


    db.add(record)
    db.commit()

    db.close()

    print(
        f"Stored transaction is", transaction
    )