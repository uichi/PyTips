import numpy as np
import matplotlib.pyplot as plt
 
x = np.random.rand(50)
y = np.random.rand(50)

plt.subplot(2,3,1)
plt.scatter(x, y)

#サイズ、色、不透明度、線のサイズ、色を指定
plt.subplot(2,3,2)
plt.scatter(x, y, s=600, c="pink", alpha=0.5, linewidths="2", edgecolors="red")

#マーカーを星にする
plt.subplot(2,3,3)
plt.scatter(x, y, s=600, c="yellow", marker="*", alpha=0.5, linewidths="2", edgecolors="orange")

#軸の名前とグリッドを指定
plt.subplot(2,3,4)
plt.scatter(x, y)
plt.title("This is a title")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)

# 乱数を 100 件生成
plt.subplot(2,3,5)
value = np.random.rand(50)
# 散布図を表示
plt.scatter(x, y, s=100, c=value, cmap='Blues')
# カラーバーを表示
plt.colorbar()

#上記の正規化
plt.subplot(2,3,6)
plt.scatter(x, y, s=100, c=value, cmap='Blues', vmin=0.4, vmax=0.6)
plt.colorbar()

plt.show()