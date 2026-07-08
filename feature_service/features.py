from feature_service.redis_store import RedisStore
from common.models import UserProfileForFS
from common.models import Transaction

class Features:

    def __init__(self, transaction):
        self.r = RedisStore()
        self.transaction = transaction
        
        
    def amount_ratio(self): 
        if self.r.profile_exists(self.transaction['sender_id']):
            self.user_profile_fs = self.r.get_user_profile(self.transaction['sender_id'])
            new_avg = (float(self.user_profile_fs["avg_amount"]) + transaction['amount'] )
            
            ratio = (self.transaction['amount'] /float(self.user_profile_fs["avg_amount"]))
            
            self.user_profile_fs["avg_amount"] = (float(self.user_profile_fs["avg_amount"]) + self.transaction['amount'] )
            self.user_profile_fs["transaction_count"] = int(self.user_profile_fs["transaction_count"]) + 1
            self.user_profile_fs["timestamp"] = self.transaction["timestamp"]
            self.user_profile_fs["last_device"] = self.transaction["last_device"]
            self.user_profile_fs["last_city"] = self.transaction["last_city"]

            self.r.update_user(self.user_profile_fs)

            return ratio
        else:
            self.r.set_user(transaction)    
            return 1

 
