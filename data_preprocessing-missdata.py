import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 讀取數據
df = pd.read_csv(r"C:\Users\brigh\train.csv")

df.isnull().sum()