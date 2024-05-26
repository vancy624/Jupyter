import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 讀取數據
data = pd.read_csv(r"C:\Users\brigh\data_test.csv")
#data = pd.read_csv(r"C:\Wenhuiii___code\Jupyter\202404_weather_data.csv", header=1, usecols=[1,2,4,6,11,14,19])

# 將非數值轉成NaN
data = data.apply(pd.to_numeric, errors='coerce')

# 計算相關係數矩陣
correlation_matrix = data.corr()

# 繪製相關係數熱力圖
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, cmap='YlGnBu')
#sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()