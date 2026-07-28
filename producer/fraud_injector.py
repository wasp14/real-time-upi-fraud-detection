import random
from common.constants import CITIES, MERCHANTS
from producer.modes import SimulationMode


class FraudInjector:

    FRAUD_RATE = 0.05

    def inject(self, transaction, simulator, SENDER ):

        mode = simulator.mode

        if mode == SimulationMode.NORMAL:
            return transaction

        elif mode == SimulationMode.TRAINING:

            if random.random() > self.FRAUD_RATE:
                transaction.is_fraud = False
                return transaction


            scenario = random.choices([
                self.account_takeover,
                self.merchant_scam,
                self.velocity_attack,
                self.device_swap
            ],
            weights=[30, 35, 20, 15],
            k=1
            )[0]


            return scenario(transaction, simulator, SENDER )

        elif mode == SimulationMode.VELOCITY_TEST:
            return self.velocity_attack(transaction, simulator, SENDER)

        elif mode == SimulationMode.MERCHANT_TEST:
            return self.merchant_scam(transaction, simulator=None, sender=Noner)

        elif mode == SimulationMode.ACCOUNT_TEST:
            return self.account_takeover(transaction, simulator=None, sender=None)

        return transaction



    def account_takeover(self, transaction, simulator=None, sender=None):

        transaction.is_fraud = True

        transaction.amount = round(
            transaction.amount * random.uniform(5, 8),
            2
        )

        new_city = random.choice(CITIES)

        while new_city == transaction.city:
            new_city = random.choice(CITIES)

        transaction.city = new_city

        transaction.device_id = f"DEV{random.randint(1000,9999)}"

        new_merchant = random.choice(MERCHANTS)

        while new_merchant[0] == transaction.merchant:
            new_merchant = random.choice(MERCHANTS)

        transaction.merchant = new_merchant[0]
        transaction.merchant_category = new_merchant[1]

        return transaction



    def merchant_scam(self, transaction, simulator=None, sender=None):

        transaction.is_fraud = True

        new_merchant = random.choice(MERCHANTS)

        while new_merchant[0] == transaction.merchant:
            new_merchant = random.choice(MERCHANTS)

        transaction.amount = round(
            transaction.amount * random.uniform(1.5, 3),
            2
        )

        transaction.merchant = new_merchant[0]
        transaction.merchant_category = new_merchant[1]

        return transaction



    def device_swap(self, transaction,simulator=None, sender=None):

        transaction.is_fraud = True

        transaction.device_id = f"DEV{random.randint(1000,9999)}"

        return transaction



    def velocity_attack(self, transaction, simulator, sender):

        transaction.is_fraud = True

        simulator.velocity_sender = sender
        simulator.velocity_remaining = random.randint(15,25)

        return transaction