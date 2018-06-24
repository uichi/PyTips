import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(50, 10, 1000)

#棒の数を指定(デフォルトは10)
plt.subplot(2,3,1)
plt.hist(x, bins=50)

#範囲指定
plt.subplot(2,3,2)
plt.hist(x, range=(50, 100))

#正規化
plt.subplot(2,3,3)
plt.hist(x, normed=True)

#累積値を出力
plt.subplot(2,3,4)
plt.hist(x, cumulative=True)

#ヒストグラムの下に余白を入れる
plt.subplot(2,3,5)
plt.hist(x, bottom=30)

#縦軸を対数で表示
plt.subplot(2,3,6)
plt.hist(x, log=True)

plt.show()
