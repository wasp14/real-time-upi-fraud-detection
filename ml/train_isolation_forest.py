import pandas as pd
from ml.metrics import save_metrics
from sklearn.ensemble import IsolationForest
from ml.save_model import save_model
from ml.config import ISOLATION_MODEL
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)
from ml.preprocess import prepare_data
from ml.config import RANDOM_STATE


dataset_path = "ml/fraud_detection.csv"

X_train, X_test, y_train, y_test = prepare_data(dataset_path)

model = IsolationForest(
    contamination = 0.05,
    random_state = 42,
    n_estimators = 200
)

model.fit(X_train)

predictions = model.predict(X_test)

predictions = [1 if p == -1 else 0 for p in predictions]

metrics = {
    "model": "isolation_forest",
    "accuracy": accuracy_score(y_test, predictions),
    "precision": precision_score(y_test, predictions),
    "recall": recall_score(y_test, predictions),
    "f1": f1_score(y_test, predictions),
}


save_metrics(metrics, "isolation_forest.json")
save_model(model, ISOLATION_MODEL)