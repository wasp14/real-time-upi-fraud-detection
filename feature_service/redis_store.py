import redis
from common.models import UserProfileForFS
from common.models import Transaction
class RedisStore:
    def __init__(self):
        self.r = redis.Redis(host = 'localhost', port = 6379, decode_responses = True)

    def profile_exists(self, user_id):
        return self.r.exists(user_id)

    def get_user_profile(self, user_id):
        return self.r.hgetall(user_id)

    def set_user(self, transaction):
        self.r.hset(transaction['sender_id'], 
        mapping = {"avg_amount": transaction['amount'],
                   "last_transaction_time": transaction['timestamp'],
                   "transaction_count": 1,
                   "last_device": transaction['device_id'],
                   "last_city": transaction['city']} )  
      
    def update_user(self, transaction):
        self.r.hset(transaction['sender_id'],
          mapping={ "avg_amount": transaction['avg_amount'],
                    "last_transaction_time": transaction['timestamp'],
                    "transaction_count": transaction['transaction_count'],
                    "last_device": transaction['device_id'],
                    "last_city": transaction['city']    
                    })