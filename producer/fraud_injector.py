import random
from common.constants import CITIES, MERCHANTS


class FraudInjector:

    FRAUD_RATE = 0.05

    def inject(self, transaction):
        
        # 95% Normal Transactions
        if random.random() > self.FRAUD_RATE:
            transaction.is_fraud = False
            return transaction

        # Fraud Transaction
        transaction.is_fraud = True

        scenario = random.choice([
            self.account_takeover,
            self.merchant_scam
        ])

        return scenario(transaction)

    def account_takeover(self, transaction):
        """
        Simulates an account takeover:
        - High amount
        - New city
        - New device
        - New merchant
        """

        # High Amount
        transaction.amount = round(
            transaction.amount * random.uniform(5, 8),
            2
        )

        # New City
        new_city = random.choice(CITIES)
        while new_city == transaction.city:
            new_city = random.choice(CITIES)
        transaction.city = new_city

        # New Device
        transaction.device_id = f"DEV{random.randint(1000, 9999)}"

        # New Merchant
        new_merchant = random.choice(MERCHANTS)
        while new_merchant[0] == transaction.merchant:
            new_merchant = random.choice(MERCHANTS)

        transaction.merchant = new_merchant[0]
        transaction.merchant_category = new_merchant[1]

        return transaction

    def merchant_scam(self, transaction):
        """
        Simulates a payment to an unknown merchant.
        """

        new_merchant = random.choice(MERCHANTS)

        while new_merchant[0] == transaction.merchant:
            new_merchant = random.choice(MERCHANTS)

        transaction.merchant = new_merchant[0]
        transaction.merchant_category = new_merchant[1]

        return transaction