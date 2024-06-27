import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 3)

# 在每個子圖上繪製數據
for i, ax in enumerate(axs.flat):
    ax.plot([0, 1, 2, 3], [i, i**2, i**3, i**4])
    ax.set_title(f'Plot {i+1}')

# 調整子圖之間的間距
fig.subplots_adjust(hspace=0.5, wspace=0.5)

# 顯示圖形
plt.show()
