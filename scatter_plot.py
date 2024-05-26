import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np

#檔案讀取，並忽略標題(header)，並從第二列資料開始讀取 (usecols:指定文件從第幾行開始讀取)
df_temp = pd.read_csv(r"C:\Users\brigh\202404_TEMP.csv", usecols=range(1, 24))
df_rh = pd.read_csv(r"C:\Users\brigh\202404_RH.csv", usecols=range(1, 24))
# df_temp = pd.read_csv(r"C:\Users\brigh\202404_TEMP.csv", header=0, usecols=range(1, 24))
# df_rh = pd.read_csv(r"C:\Users\brigh\202404_RH.csv", header=0, usecols=range(1, 24))
#print(df_temp.columns)

# 將DataFrame中的所有值轉換成數字，非數字的資料會被轉成NaN   #再將NaN轉成0   .fillna(0)
df_temp = df_temp.apply(pd.to_numeric, errors='coerce')
df_rh = df_rh.apply(pd.to_numeric, errors='coerce')

# 將DataFrame的值轉換為一維列表
values_list_temp = df_temp.values.flatten().tolist()
values_list_rh = df_rh.values.flatten().tolist()
#print(values_list_temp)

plt.scatter(values_list_temp,values_list_rh)
plt.xlabel("Temperature") #X軸標簽
plt.ylabel("RH") #Y軸標簽
plt.grid(True) #在圖表中顯示網格線
plt.show()


#header=0 (默認)
#表示文件的第一列（索引為0的行）應該被當作行標題。 (標題不會被讀取)

#header=None 
#表示會在每"行"每"列"前都加入標題，讓原始csv檔所有格都被讀進去
#表示文件中沒有任何行應該被當作列標題。pandas會自動為列分配數字標籤，從0開始。

#header=1 
#csv中的第二列會變成行標題
 
#usecols 可用來指定要讀取的"行"

#skiprows 跳過列