import redis
from common.models import UserProfileForFS
from common.models import Transaction
class RedisStore:
    def __init__(self):
        self.r = redis.Redis(host = 'localhost', port = 6379, decode_responses = True)

    def profile_exists(self, user_id):
        return self.r.exists(user_id)

    def get_user_profile(self, user_id):
        profile = self.r.hgetall(user_id)
        user_profile_fs = UserProfileForFS(**profile)
        return user_profile_fs

    def set_user(self, transaction):
        self.r.hset(transaction.sender_id, 
        mapping = {"avg_amount": transaction.amount,
                   "last_transaction_time": transaction.timestamp,
                   "transaction_count": 1,
                   "last_device": transaction.device_id,
                   "last_city": transaction.city,
                   "last_merchant" :  transaction.merchant} )  
      
    def update_user(self, sender_id, user_profile_fs):
        self.r.hset(sender_id,
          mapping={ "avg_amount": user_profile_fs.avg_amount,
                    "last_transaction_time": user_profile_fs.last_transaction_time,
                    "transaction_count": user_profile_fs.transaction_count,
                    "last_device": user_profile_fs.last_device,
                    "last_city": user_profile_fs.last_city ,
                    "last_merchant": user_profile_fs.last_merchant  
                    })