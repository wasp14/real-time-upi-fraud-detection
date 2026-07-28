import pandas as pd
from sklearn.model_selection import train_test_split

from ml.config import (
    FEATURE_COLUMNS,
    TARGET,
    TEST_SIZE,
    RANDOM_STATE
)

def load_dataset(csv_path):
    return pd.read_csv(csv_path)


def get_features_target(df):
    x = df[FEATURE_COLUMNS]
    y = df[TARGET]

    return x,y


def split_dataset(X,Y):
    
    return train_test_split(
        X,
        y,
        test_size = TEST_SIZE,
        random_state = RANDOM_STATE,
        stratify = y
    )


def prepare_xgboost(csv_path):
    df = load_dataset(csv_path)
    X, y  = get_features_target(df)
    return split_dataset(X,y)

def prepare_isolation_forest(csv_path):
    
    df = load_dataset(csv_path)

    X = df[FEATURE_COLUMNS]
    
    y = df[TARGET]

    x_train = X[ y == False]