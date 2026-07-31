import pandas as pd

from sklearn.model_selection import train_test_split

from ml.config import (
    FEATURE_COLUMNS,
    TARGET,
    TEST_SIZE,
    RANDOM_STATE
)


def load_dataset(path):

    df = pd.read_csv(path)

    return df



def prepare_data(path):

    df = load_dataset(path)

    X = df[FEATURE_COLUMNS]

    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y
    )

    return (
        X_train,
        X_test,
        y_train,
        y_test
    )