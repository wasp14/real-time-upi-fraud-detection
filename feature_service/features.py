from feature_service.redis_store import RedisStore
from common.models import UserProfileForFS
from common.models import Transaction
from common.models import UserProfileForFS
from datetime import datetime
import time
from common.models import  EnrichedTransaction

class Features:

    def __init__(self, transaction):
        self.r = RedisStore()
        self.transaction = transaction
        if self.r.profile_exists(self.transaction.sender_id):
            self.user_profile_fs = self.r.get_user_profile(self.transaction.sender_id)
        else:
            self.r.set_user(transaction)
            self.user_profile_fs = self.r.get_user_profile(self.transaction.sender_id)

    def amount_ratio(self): 
        print("Avg:", self.user_profile_fs.avg_amount)
        print("Amount:", self.transaction.amount)
        ratio = (self.transaction.amount /float(self.user_profile_fs.avg_amount))
        print("Ratio:", ratio)
        ratio = round(ratio,2)
        return ratio

    def time_since_last_txn(self):

           self.user_profile_fs = self.r.get_user_profile(self.transaction.sender_id)
           last = datetime.fromisoformat(self.user_profile_fs.last_transaction_time)
           current = datetime.fromisoformat(self.transaction.timestamp)

           time_diff = current - last
           return round(time_diff.total_seconds(), 2)

    def update_profile(self):
            old_count = int(self.user_profile_fs.transaction_count)
            old_avg = float(self.user_profile_fs.avg_amount)
            new_count = old_count + 1
            new_avg = (old_avg * old_count + self.transaction.amount) / new_count
            self.user_profile_fs.last_transaction_time = self.transaction.timestamp
            self.user_profile_fs.last_device = self.transaction.device_id
            self.user_profile_fs.last_city = self.transaction.city
            self.user_profile_fs.last_merchant = self.transaction.merchant
            self.r.update_user(self.transaction, self.user_profile_fs)

    def device_changed(self):
        return  self.transaction.device_id != self.user_profile_fs.last_device 

    def city_changed(self):
        return  self.transaction.city != self.user_profile_fs.last_city 

    def merchant_changed(self):
        return  self.transaction.merchant != self.user_profile_fs.last_merchant 

    def txn_velocity(self):
        count = self.r.txn_velocity(self.transaction)

        return count

    def compute_features(self):
        amount_ratio = self.amount_ratio()
        time_since_last_txn = self.time_since_last_txn()
        device_changed = self.device_changed()
        city_changed = self.city_changed()
        merchant_changed = self.merchant_changed()
        txn_velocity = self.txn_velocity()

        features = {"amount_ratio" : amount_ratio,
                    "time_since_last_txn": time_since_last_txn,
                    "device_changed": device_changed,
                    "merchant_changed": merchant_changed,
                    "city_changed" : city_changed,
                    "txn_velocity" : txn_velocity}

        enriched_transaction = EnrichedTransaction(
            transaction_id = self.transaction.transaction_id,
            sender_id  = self.transaction.sender_id,
            receiver_id  = self.transaction.receiver_id,
            amount = self.transaction.amount,
            amount_ratio = features['amount_ratio'],
            time_since_last_txn = features['time_since_last_txn'],
            device_changed = features['device_changed'],
            city_changed = features['city_changed'],
            merchant_changed = features['merchant_changed'],
            txn_velocity = txn_velocity,
            is_fraud = self.transaction.is_fraud

            )            
        self.update_profile()            
        return enriched_transaction




