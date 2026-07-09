from feature_service.redis_store import RedisStore
from common.models import UserProfileForFS
from common.models import Transaction
from common.models import UserProfileForFS
from datetime import datetime

class Features:

    def __init__(self, transaction):
        self.r = RedisStore()
        self.transaction = transaction
        if self.r.profile_exists(self.transaction.sender_id):
            self.user_profile_fs = self.r.get_user_profile(self.transaction.sender_id)
        else:
            self.r.set_user(transaction)

        
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
            self.r.update_user(self.transaction.sender_id, self.user_profile_fs)


    def device_changed(self):
        return if self.transaction.device_id != self.user_profile_fs.last_device 

    def city_changed(self):
        return if self.transaction.city != self.user_profile_fs.last_city 

    def merchant_cahnged(self):
        return if self.transaction.merchant != self.user_profile_fs.last_merchant 

    def compute_features(self):


