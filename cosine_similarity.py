# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from math import sqrt

csv = input("読み込むｃｓｖファイルを入力してください。 : ")
table = pd.read_csv(csv, encoding='utf-8')
# カラムリスト作成
items = []
for i in range(1, len(table.columns)):
    items.append(table.columns[i:i+1][0])

taste_dict = {}
for item in items:
    item_taste = []
    for i in range(len(items)):
        item_taste.append(table[item][i])
    taste_dict[item] = item_taste

# taste = pd.Series(taste_dict)

# 趣向データのベクトル化
everything_vector = {}
for i in range(len(taste_dict)):
    taste_vector = []
    # for color in taste.index:
    for color in taste_dict.keys():
        vector = 0
        # for j in range(len(taste[color])):
        for j in range(len(taste_dict[color])):
            # if taste[i][j] == taste[color][j] and taste[i][j] == 1:
            if taste_dict[color][j] == taste_dict[color][j] and taste_dict[i][j] == 1:
                vector += 1
        taste_vector.append(vector)
    all_vector[color] = taste_vector
# all_vector = pd.Series(everything_vector)
df_vector = pd.DataFrame(all_vector, index=all_vector.keys())
df_vector.to_csv('vector_' + csv, encoding='utf-8')

exit()
# 趣向ベクトルからコサイン類似度を算出
cosine_similarity = {}
for i in range(len(all_vector)):
    vector = []
    q_vector = np.linalg.norm(all_vector[i])
    for nan_times in range(i):
        vector.append(np.nan)
    for j in range(i, len(all_vector)):
        r_vector = np.linalg.norm(all_vector[j])
        qr_vector = np.dot(all_vector[i], all_vector[j])
        vector.append(round(qr_vector/(q_vector*r_vector), 2))
    cosine_similarity[all_vector.index[i]] = vector

df = pd.DataFrame(cosine_similarity)
df = df.T
df.columns = cosine_similarity.keys()
df.to_csv('similarity_' + csv, encoding='utf-8')
