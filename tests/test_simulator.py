from producer.simulator import TransactionSimulator
from common.models import Transaction


def test_generate_transaction_returns_transaction():

    simulator = TransactionSimulator()

    transaction = simulator.generate_transaction()

    assert isinstance(transaction, Transaction)


def test_transaction_has_unique_id():

    simulator = TransactionSimulator()

    transaction1 = simulator.generate_transaction()
    transaction2 = simulator.generate_transaction()

    assert transaction1.transaction_id != transaction2.transaction_id


def test_sender_and_receiver_are_different():

    simulator = TransactionSimulator()

    transaction = simulator.generate_transaction()

    assert transaction.sender_id != transaction.receiver_id


def test_transaction_amount_is_valid():

    simulator = TransactionSimulator()

    transaction = simulator.generate_transaction()

    assert transaction.amount >= 50


def test_transaction_has_required_fields():

    simulator = TransactionSimulator()

    transaction = simulator.generate_transaction()

    assert transaction.transaction_id
    assert transaction.sender_id
    assert transaction.receiver_id
    assert transaction.timestamp
    assert transaction.merchant
    assert transaction.payment_mode