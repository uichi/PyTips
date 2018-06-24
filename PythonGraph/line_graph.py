import numpy as np
import matplotlib.pyplot as plt
 
left = np.array([1, 2, 3, 4, 5])
height = np.array([0, 2, 4, 2, 6])

plt.subplot(4, 2, 1)
plt.plot(left, height)

#千の太さを４、色を赤
plt.subplot(4, 2, 2)
plt.plot(left, height, linewidth=4, color="red")

#実線、破線、破線点線、点線
plt.subplot(4, 2, 3)
plt.plot(left, height, linestyle="solid")
plt.plot(left, height/2, linestyle="dashed")
plt.plot(left, height/3, linestyle="dashdot")
plt.plot(left, height/4, linestyle="dotted")

#丸印のマーカーを付ける
plt.subplot(4, 2, 4)
plt.plot(left, height, marker="o")

#丸印のマーカーを付ける
plt.subplot(4, 2, 5)
plt.plot(left, height, marker="o", markeredgewidth=0)

#マーカーをダイヤモンド型 (D)、サイズ 12、マーカーの枠線のサイズ 3、マーカーの枠線の色 青、マーカーの塗りつぶしの色を水色で出力
plt.subplot(4, 2, 6)
plt.plot(left, height, marker="D", markersize=12, markeredgewidth=3, markeredgecolor="blue",markerfacecolor="lightblue")

#マーカーをダイヤモンド型 (s)、サイズ 12、マーカーの枠線のサイズ 3、マーカーの枠線の色 青、マーカーの塗りつぶしの色1 青、マーカーの塗りつぶしの色2 赤、マーカーの塗りつぶし方法 左半分で出力
plt.subplot(4, 2, 7)
plt.plot(left, height, marker="s", markersize=20, markeredgewidth=2, markeredgecolor="black",  markerfacecolor="blue", markerfacecoloralt="red", fillstyle="left")

#アンチエイリアス
plt.subplot(4, 2, 8)
plt.plot(left, height, linewidth=5, antialiased=False)
plt.plot(left, height/2, linewidth=5)

plt.show()