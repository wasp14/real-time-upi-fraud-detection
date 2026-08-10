from types import SimpleNamespace

from feature_service.features import Features


def test_amount_ratio():

    features = Features.__new__(Features)

    features.transaction = SimpleNamespace(
        amount=500.0
    )

    features.user_profile_fs = SimpleNamespace(
        avg_amount=250.0
    )

    result = features.amount_ratio()

    assert result == 2.0

def test_device_changed():

    features = Features.__new__(Features)

    features.transaction = SimpleNamespace(
        device_id="DEVICE_002"
    )

    features.user_profile_fs = SimpleNamespace(
        last_device="DEVICE_001"
    )

    assert features.device_changed() is True



def test_device_not_changed():

    features = Features.__new__(Features)

    features.transaction = SimpleNamespace(
        device_id="DEVICE_001"
    )

    features.user_profile_fs = SimpleNamespace(
        last_device="DEVICE_001"
    )

    assert features.device_changed() is False