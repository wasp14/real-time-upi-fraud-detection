TARGET = 'is_fraud'

FEATURE_COLUMNS = [

    "amount_ratio",
    "transaction_velocity",
    "device_changed",
    "city_changed",
    "merchant_changed"
]


TEST_SIZE = 0.2

RANDOM_STATE = 42

MODEL_DIR ="ml/models"

XGBOOST_MODEL = "xgboost.pkl"

ISOLATION_MODEL = "isolation_forest.pkl"