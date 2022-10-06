#N = int(input())
import numpy as np


N = 3

list1 = [['-'] * N for i in range(N)]# 2次元配列の宣言方法は必ずこれ!
print(list1)
list1[1][2] = 1
print(list1)
# リスト中に文字列と数字が混在できることに気付いた。

list = [[0] * 3] * 3
print(list)
list[1][2] = 1
print(list)

list2 = [[0 for i in range(3)] for j in range(4)]
print(list2)
list2[3][2] = 1
print(list2)

# numpyを使って定義できるのはリストではなく配列！！！
list3 = np.zeros((3, 3))
print(list3)
list3[1][2] = 1
print(list3)
