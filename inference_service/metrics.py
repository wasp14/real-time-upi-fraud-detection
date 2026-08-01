from prometheus_client import Histogram, Counter

transactions_processed = Counter(
    "transactions_processed_total",
    "Total transactions processed"
)

fraud_predictions = Counter(
    "fraud_predictions",
    "Total fraud predictions"
)

normal_predictions = Counter(
    "normal_predictions",
    "Total normal predictions"
)

alerts_published = Counter(
    "alerts_predictions_total",
    "Total alerts published"
)

prediction_latency = Histogram(
    "prediction_latency_seconds",
    "Time taken for predictions"
)

fraud_probability = Histogram(
    "fraud_probability",
    "Distribution of fraud prediction probabilities",
    buckets=(0.0, 0.2, 0.4, 0.6, 0.8, 0.9, 0.95, 1.0)
)