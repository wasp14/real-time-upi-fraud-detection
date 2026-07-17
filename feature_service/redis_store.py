import redis
from common.models import UserProfileForFS
from common.models import Transaction
import time


class RedisStore:
    def __init__(self):
        self.r = redis.Redis(host = 'localhost', port = 6379, decode_responses = True)

    def profile_exists(self, user_id):
        return self.r.exists(user_id)

    def get_user_profile(self, user_id):
        data = self.r.hgetall(user_id)
        return UserProfileForFS.from_redis(data)

    def set_user(self, transaction):
        self.r.hset(transaction.sender_id, 
        mapping = {"avg_amount": transaction.amount,
                   "last_transaction_time": transaction.timestamp,
                   "transaction_count": 1,
                   "last_device": transaction.device_id,
                   "last_city": transaction.city,
                   "last_merchant" :  transaction.merchant} )  

        self.r.zadd(f"velocity:{transaction.sender_id}",    {
        transaction.transaction_id: time.time()
    })       

    def txn_velocity(self, transaction):
        current_time = time.time()
        self.r.zremrangebyscore(f"velocity:{transaction.sender_id}","-inf",current_time - 60)

        count = self.r.zcard(f"velocity:{transaction.sender_id}")
        return count        
      
    def update_user(self, transaction, user_profile_fs):
        self.r.hset(transaction.sender_id   ,
          mapping={ "avg_amount": user_profile_fs.avg_amount,
                    "last_transaction_time": user_profile_fs.last_transaction_time,
                    "transaction_count": user_profile_fs.transaction_count,
                    "last_device": user_profile_fs.last_device,
                    "last_city": user_profile_fs.last_city ,
                    "last_merchant": user_profile_fs.last_merchant  
                    })

        self.r.zadd(f"velocity:{transaction.sender_id}",    {
        transaction.transaction_id: time.time()
    })                