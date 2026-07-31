import joblib
import pandas as pd
import shap
from inference_service.schema import FeatureContribution
from ml.config import (
    XGBOOST_MODEL,
    FEATURE_COLUMNS,
    MODEL_DIR
)


class FraudPredictor:
    def __init__(self):
        self.model = joblib.load(f"{MODEL_DIR}/{XGBOOST_MODEL}")
        self.explainer = shap.TreeExplainer(self.model)


    def prepare_data(self, features):
        df = pd.DataFrame(
            [features], FEATURE_COLUMNS
        )
        return df



    def explain(self, df):

        explanation = self.explainer(df)
        shap_values = explanation[0].values
        feature_impact = []

        for feature, impact in zip(FEATURE_COLUMNS,shap_values ):
            feature_impact.append({
                "feature": feature,
                "impact": round(float(impact),2)
            })

        feature_impact.sort(
            key = lambda x : abs(x["impact"]),
            reverse = True
        )

        return feature_impact




    def predict(self, features):

        input_df = self.prepare_data(features)

        feature_impact = self.explain(input_df)
        
        probability = self.model.predict_proba(input_df)[0][1]    
        prediction = self.model.predict(input_df)[0]

        feature_impact = self.explain(input_df)
        

        return {
            "prediction" : "Fraud" if prediction == 1 else "Normal",
            "probability" : round(float(probability),2),
            "top_features" : feature_impact  
        }