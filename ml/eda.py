import pandas as pd
import matplotlib.pyplot as plt 


df = pd.read_csv('ml/fraud_detection.csv')

print(df.head())
# print(df.info())
# print(df.describe())
# print(df["is_fraud"].unique())
# print(df.dtypes)
print(df.isnull().sum())