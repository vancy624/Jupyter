import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np

#檔案讀取
df = pd.read_csv("data_test.csv")
#print(df.columns)


#先創一個新的DataFrame來存每個項目每月平均值
monthly_averages = pd.DataFrame()

features = ['pm2.5', 'DEWP', 'TEMP', 'PRES', 'Iws', 'Is', 'Ir']

# 算出每月每個特徵的平均
for feature in features:
    # 计算每个特征每月的平均值，并添加到monthly_averages DataFrame中
    monthly_averages[feature] = df.groupby('month')[feature].mean()

# 使用ggplot主題樣式
plt.style.use("ggplot")               

# 定義每條線顏色
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

#設置x軸刻度的位置為1-12月
months = range(1, 13)
plt.xticks(months)

#繪出每月每個特徵折線圖
for i, feature in enumerate(features): #將特徵列表中的每個特徵及其索引提供給for迴圈
    plt.plot(monthly_averages.index, monthly_averages[feature], c=colors[i])

#添加圖例(每條線代表什麼，並將圖例放置最佳位置)
plt.legend(labels=['pm2.5', 'DEWP', 'TEMP', 'PRES', 'Iws', 'Is','Ir'], loc = 'best') 
# 設定x軸標題及粗體
plt.xlabel("months", fontweight = "bold") 
# 設定y軸標題及粗體
plt.ylabel(" Average of feature", fontweight = "bold") 
# 設定圖表標題及粗體
plt.title("2014 Monthly average change", fontsize=15, fontweight="bold")

plt.show()




#算出每月之每個項目的平均
# pm25_monthly_average = df.groupby('month')['pm2.5'].mean()
# DEWP_monthly_average = df.groupby('month')['DEWP'].mean()
# TEMP_monthly_average = df.groupby('month')['TEMP'].mean()
# PRES_monthly_average = df.groupby('month')['PRES'].mean()
# Iws_monthly_average = df.groupby('month')['Iws'].mean()
# Is_monthly_average = df.groupby('month')['Is'].mean()
# Ir_monthly_average = df.groupby('month')['Ir'].mean()

# 將結果轉換為 DataFrame
# pm25_monthly_average_df = pm25_monthly_average.reset_index()
# DEWP_monthly_average_df = DEWP_monthly_average.reset_index()
# TEMP_monthly_average_df = TEMP_monthly_average.reset_index()
# PRES_monthly_average_df = PRES_monthly_average.reset_index()
# Iws_monthly_average_df = Iws_monthly_average.reset_index()
# Is_monthly_average_df = Is_monthly_average.reset_index()
# Ir_monthly_average_df = Ir_monthly_average.reset_index()

 # 使用ggplot主題樣式
# plt.style.use("ggplot")              

# colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
# months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# plt.xticks(months)

# plt.plot(pm25_monthly_average_df['month'], pm25_monthly_average_df['pm2.5'], c = colors[0])
# plt.plot(DEWP_monthly_average_df['month'], DEWP_monthly_average_df['DEWP'], c = colors[1])
# plt.plot(TEMP_monthly_average_df['month'], TEMP_monthly_average_df['TEMP'], c = colors[2])
# plt.plot(PRES_monthly_average_df['month'], PRES_monthly_average_df['PRES'], c = colors[3])
# plt.plot(Iws_monthly_average_df['month'], Iws_monthly_average_df['Iws'], c = colors[4])
# plt.plot(Is_monthly_average_df['month'], Is_monthly_average_df['Is'], c = colors[5])
# plt.plot(Ir_monthly_average_df['month'], Ir_monthly_average_df['Ir'], c = colors[6])
