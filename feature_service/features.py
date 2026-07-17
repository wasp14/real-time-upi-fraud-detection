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

            
            ratio = (self.transaction.amount /float(self.user_profile_fs.avg_amount))

            return ratio


    def time_since_last_txn(self):

           self.user_profile_fs = self.r.get_user_profile(self.transaction.sender_id)
           last = datetime.fromisoformat(self.user_profile_fs.last_transaction_time)
           current = datetime.fromisoformat(self.transaction.timestamp)

           time_diff = current - last
           return time_diff.total_seconds()

    def update_profile(self):
            self.user_profile_fs.transaction_count = int(self.user_profile_fs.transaction_count) + 1
            self.user_profile_fs.avg_amount = (float(self.user_profile_fs.avg_amount) + self.transaction.amount )/float(self.user_profile_fs.transaction_count)
            self.user_profile_fs.timestamp = self.transaction.timestamp
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
            txn_velocity = txn_velocity

    )            
        self.update_profile()            
        return enriched_transaction




