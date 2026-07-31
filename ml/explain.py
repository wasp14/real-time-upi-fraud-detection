import os
import joblib
import shap
import matplotlib.pyplot as plt
from ml.save_model import load_model

from ml.config import (
    FEATURE_COLUMNS,
    XGBOOST_MODEL
)

from ml.preprocess import prepare_data


dataset_path = "ml/fraud_detection.csv"

model = load_model(XGBOOST_MODEL)

_, X_test, _, y_test = prepare_data(dataset_path)


explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

print(X_test.shape)
print(shap_values.shape)


os.makedirs("ml/plots", exist_ok= True)

shap.summary_plot(
    shap_values,
    X_test,
    feature_names =  FEATURE_COLUMNS,
    show = False
)

plt.tight_layout()
plt.savefig("ml/plots/summary.png", dpi = 300)
plt.close()

predictions = model.predict(X_test)

fraud_indices = []

for i,pred in enumerate(predictions):
    if pred == 1:
        fraud_indices.append(i)


id = fraud_indices[0]

explanation = explainer(X_test)

shap.plots.waterfall(
    explanation[id],
    show = False
)

plt.tight_layout()
plt.savefig("ml/plots/waterfall_plot.png", dpi = 300)
plt.close()
