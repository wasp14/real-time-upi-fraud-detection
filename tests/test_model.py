import pandas as pd

from inference_service.predictor import FraudPredictor
from ml.config import FEATURE_COLUMNS


def test_prepare_data():

    predictor = FraudPredictor.__new__(FraudPredictor)

    features = {
        "amount_ratio": 2.0,
        "time_since_last_txn": 30.0,
        "device_changed": True,
        "city_changed": False,
        "merchant_changed": True,
        "txn_velocity": 5
    }

    result = predictor.prepare_data(features)

    assert isinstance(result, pd.DataFrame)
    assert list(result.columns) == FEATURE_COLUMNS
    assert len(result) == 1


class FakeModel:

    def predict_proba(self, df):
        return [[0.2, 0.8]]

    def predict(self, df):
        return [1]


class FakeExplainer:

    def __call__(self, df):

        class Explanation:
            values = [0.5, -0.2, 0.1, 0.05, -0.03, 0.01]

        return [Explanation()]


def test_predict_returns_expected_output():

    predictor = FraudPredictor.__new__(FraudPredictor)

    predictor.model = FakeModel()
    predictor.explainer = FakeExplainer()

    features = {
        "amount_ratio": 2.0,
        "time_since_last_txn": 30.0,
        "device_changed": True,
        "city_changed": False,
        "merchant_changed": True,
        "txn_velocity": 5
    }

    result = predictor.predict(features)

    assert result["prediction"] == "Fraud"
    assert result["probability"] == 0.8
    assert len(result["top_features"]) == len(FEATURE_COLUMNS)