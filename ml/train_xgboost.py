import pandas as pd
from ml.metrics import save_metrics
from xgboost import XGBClassifier
from ml.save_model import save_model
from ml.config import XGBOOST_MODEL
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

negative = (y_train == 0).sum()
positive = (y_train == 1).sum()

scale_pos_weight = negative / positive

print(scale_pos_weight)


model = XGBClassifier(
    n_estimators = 200,
    learning_rate = 0.05,
    max_depth = 5,
    random_state = RANDOM_STATE,
    max_delta_step=1,
    scale_pos_weight=3
)

model.fit(X_train, y_train)

probabilities = model.predict_proba(X_test)[:, 1]
predictions = (probabilities >= 0.3).astype(int)

metrics = {
    "model": "XGBoost",
    "accuracy": accuracy_score(y_test, predictions),
    "precision": precision_score(y_test, predictions),
    "recall": recall_score(y_test, predictions),
    "f1": f1_score(y_test, predictions),
}

save_metrics(metrics, "xgboost_metrics.json")


print("Accuracy :", accuracy_score(y_test, predictions))
print("Precision:", precision_score(y_test, predictions))
print("Recall   :", recall_score(y_test, predictions))
print("F1 Score :", f1_score(y_test, predictions))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report")
print(classification_report(y_test, predictions))




importance = pd.DataFrame({
    "Feature": X_train.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print(importance)

save_model(model, XGBOOST_MODEL)