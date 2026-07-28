import joblib
from pathlib import Path
from ml.config import MODEL_DIR

def save_model(model,filename):

    Path(MODEL_DIR).mkdir(parents=True, exist_ok=True)

    joblib.dump(model, f"{MODEL_DIR}/{filename}")

    print(f"Model saved to {MODEL_DIR}/{filename}")


def load_model(filename):
    return joblib.load(f"{MODEL_DIR}/{filename}")
