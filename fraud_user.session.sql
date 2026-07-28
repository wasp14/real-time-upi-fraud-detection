SELECT column_name
FROM information_schema.columns
WHERE table_name = 'transactions';



select count(*) from transactions;

select * from transactions;



SELECT *
FROM transactions
WHERE transaction_id = 'TXN-5ebfdad8f458';


SELECT current_database();

SELECT current_schema();

SELECT COUNT(*) FROM transactions;


SELECT
COUNT(*) FILTER (WHERE is_fraud = TRUE) AS fraud,
COUNT(*) FILTER (WHERE is_fraud = FALSE) AS normal
FROM transactions;



SELECT *
FROM transactions
WHERE amount_ratio IS NULL
   OR transaction_velocity IS NULL
   OR time_since_last_txn IS NULL;


SELECT *
FROM transactions
LIMIT 10;


SELECT is_fraud, COUNT(*)
FROM transactions
GROUP BY is_fraud;

select * from transactions where is_fraud = 'TRUE';

SELECT merchant_changed, COUNT(*)
FROM transactions
GROUP BY merchant_changed;

SELECT is_fraud, COUNT(*)
FROM transactions
GROUP BY is_fraud;


SELECT
MIN(amount_ratio),
MAX(amount_ratio),
AVG(amount_ratio)
FROM transactions;


SELECT
MIN(transaction_velocity),
MAX(transaction_velocity),
AVG(transaction_velocity)
FROM transactions;



SELECT merchant_changed, COUNT(*)
FROM transactions
GROUP BY merchant_changed;



SELECT device_changed, COUNT(*)
FROM transactions
GROUP BY device_changed;


SELECT city_changed, COUNT(*)
FROM transactions
GROUP BY city_changed;


SELECT
MIN(transaction_velocity),
MAX(transaction_velocity),
AVG(transaction_velocity)
FROM transactions;

SELECT
MIN(amount_ratio),
MAX(amount_ratio),
AVG(amount_ratio)
FROM transactions;


SELECT
    is_fraud,
    AVG(amount_ratio),
    AVG(transaction_velocity),
    AVG(device_changed::int),
    AVG(city_changed::int),
    AVG(merchant_changed::int)
FROM transactions
GROUP BY is_fraud;

SELECT
    is_fraud,
    AVG(amount_ratio) AS avg_amount_ratio,
    AVG(transaction_velocity) AS avg_velocity,
    AVG(device_changed::int) AS avg_device_changed,
    AVG(city_changed::int) AS avg_city_changed,
    AVG(merchant_changed::int) AS avg_merchant_changed
FROM transactions
GROUP BY is_fraud;


SELECT COUNT(*)
FROM transactions
WHERE
    amount_ratio IS NULL
    OR transaction_velocity IS NULL
    OR time_since_last_txn IS NULL
    OR device_changed IS NULL
    OR city_changed IS NULL
    OR merchant_changed IS NULL
    OR is_fraud IS NULL;


SELECT COUNT(DISTINCT transaction_id)
FROM transactions;


COPY transactions
TO '/tmp/fraud_dataset.csv'
WITH (
    FORMAT CSV,
    HEADER TRUE
);









\copy transactions TO '/tmp/fraud_dataset.csv' CSV HEADER


SELECT
    pid,
    transaction_id,
    sender_id,
    receiver_id,
    amount,
    amount_ratio,
    time_since_last_txn,
    transaction_velocity,

    CASE
        WHEN device_changed THEN 1
        ELSE 0
    END AS device_changed,

    CASE
        WHEN city_changed THEN 1
        ELSE 0
    END AS city_changed,

    CASE
        WHEN merchant_changed THEN 1
        ELSE 0
    END AS merchant_changed,

    CASE
        WHEN is_fraud THEN 1
        ELSE 0
    END AS is_fraud

FROM transactions;