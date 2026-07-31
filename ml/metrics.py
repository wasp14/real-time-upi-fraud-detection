import json
import os

def save_metrics(metrics, filename):
    os.makedirs("ml/reports", exist_ok= True)

    with open(f"ml/reports/{filename}", "w") as file:
        json.dump(metrics, file, indent=4)