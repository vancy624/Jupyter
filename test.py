import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np

#檔案讀取 
df = pd.read_csv(r"C:\Wenhuiii___code\Jupyter\202404_weather_data.csv", header=1, usecols=[6,11])

plt.scatter(df["Temperature"],df["RH"])
plt.xlabel("Temperature") #X軸標簽
plt.ylabel("RH") #Y軸標簽
plt.grid(True)
plt.show()


#header=0 (默認)
#表示文件的第一列（索引為0的行）應該被當作行標題。 (標題不會被讀取)

#header=None 
#表示會在每"行"每"列"前都加入標題，讓原始csv檔所有格都被讀進去
#表示文件中沒有任何行應該被當作列標題。pandas會自動為列分配數字標籤，從0開始。

#header=1 
#csv中的第二列會變成行標題
 
#usecols 可用來指定要讀取的"行"