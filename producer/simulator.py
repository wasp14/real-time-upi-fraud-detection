from producer.profiles import USERS
from producer.modes import SimulationMode
from common.constants import MERCHANTS
from common.constants import PAYMENT_MODES
from common.models import Transaction
import random 
from datetime import datetime
from producer.fraud_injector import FraudInjector
import uuid


class TransactionSimulator:
    
    def __init__(self, mode=SimulationMode.TRAINING):
        self.users = random.sample(USERS, k=2)
        self.fraud_injector = FraudInjector()
        self.transaction_counter = 1
        self.mode = mode
        self.velocity_remaining = 0
        self.velocity_sender = None

    def get_sender(self):
        if self.velocity_remaining > 0:
            self.velocity_remaining -= 1
            return self.velocity_sender

        return random.choice(USERS)


    def get_receiver(self, sender):
        while True:
            receiver = random.choice(USERS)
            if receiver.user_id != sender.user_id:
                return receiver

    def get_merchant(self, sender):

        if random.random() < 0.8:
            return random.choice(sender.preferred_merchants)
    
        return random.choice(MERCHANTS) 

    def generate_amount(self,SENDER,sigma):

            while True:
                amount = random.gauss( mu=SENDER.average_transaction, sigma=sigma) 

                if 50<= amount <= SENDER.max_normal_transaction:
                    break
            
            amount = round(amount, 2)
            return amount


    def get_payment_mode(self):
        return random.choice(PAYMENT_MODES)

    def generate_transaction(self):
            
            SENDER = self.get_sender()
            RECEIVER = self.get_receiver(SENDER)
            MERCHANT = self.get_merchant(SENDER)
            PAYMENT_MODE = self.get_payment_mode()
            sigma = SENDER.average_transaction * 0.3
            amount = self.generate_amount(SENDER,sigma)
            transaction_id = f"TXN-{uuid.uuid4().hex[:12]}"
            transaction = Transaction(
                transaction_id = transaction_id,
                timestamp = datetime.now().isoformat(),
                sender_id = SENDER.user_id,
                receiver_id= RECEIVER.user_id,
                amount = amount   ,
                merchant= MERCHANT[0],
                merchant_category= MERCHANT[1],
                city= SENDER.city,
                state= SENDER.state,
                device_id= SENDER.device_id,
                payment_mode= PAYMENT_MODE,
                is_fraud = False
            )

            transaction = self.fraud_injector.inject( transaction, self, SENDER)

            self.transaction_counter += 1
            return transaction    




