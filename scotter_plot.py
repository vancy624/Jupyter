import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np

#檔案讀取，並忽略行列標題，並從第二列資料開始讀取
df_temp = pd.read_csv(r"C:\Users\brigh\202404_TEMP.csv", header=None, usecols=range(1, 24))
df_rh = pd.read_csv(r"C:\Users\brigh\202404_RH.csv", header=None, usecols=range(1, 24))
#print(df_temp.columns)

# 將DataFrame中的所有值轉換成數字，非數字的資料會被轉成NaN，再將NaN轉成0
df_temp = df_temp.apply(pd.to_numeric, errors='coerce').fillna(0)
df_rh = df_rh.apply(pd.to_numeric, errors='coerce').fillna(0)

# 將DataFrame的值轉換為一維列表
values_list_temp = df_temp.values.flatten().tolist()
values_list_rh = df_rh.values.flatten().tolist()
#print(values_list_temp)

plt.scatter(values_list_temp,values_list_rh)
plt.xlabel("Temperature") #X軸標簽
plt.ylabel("RH") #Y軸標簽
plt.grid(True) #在圖表中顯示網格線
plt.show()