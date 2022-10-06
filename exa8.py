# リストのソート
from audioop import reverse
import numpy as np


list1 = [1, 3, 6, 2, 5, 766, 3232, 37, 432]
sorted_list1 = sorted(list1)
reversed_sorted_list1 = sorted(list1, reverse=True)
print(sorted_list1)
print(reversed_sorted_list1)
# sort()は破壊的処理。つまりlist1.sort()という風に使う。ソート前は保存できない。
# reverse()も同じ破壊的処理。reversed()は非破壊的。

# ちなみに2次元配列に対してもリストのソートは可能。
list2 = [
    [1, 3, 1],
    [7, 4, 9],
    [3, 5, 2],
    [1, 1, 0],
    [4, 6, 9],
]
sorted_list2 = sorted(list2)
reversed_sorted_list2 = sorted(list2, reverse=True)
print(sorted_list2)
print(reversed_sorted_list2)

# numpyを使えば2次元配列の各行ごとにソートをかけることもできる
# ただし！！！　
# リストではなく配列にあることに注意。コーディングテストには使いずらそう。(printで出力しずらい。)

new_list2 = np.sort(list2)
print(new_list2)
#　ただし、np.sort(list2, reverse=True)はできない.各行ごとに直接降順にはできなさそう
print(np.sort(list2)[::-1])
#　1次元配列でないと上手くいかない
reversed_list = []
for i in list2:
    reversed_list += [sorted(i, reverse=True)]
print(reversed_list)

#　文字列に対してもソートをかけることが可能。
# ただし大文字は先に来る（ASCIIコード順っぽい）
str1 = "PopUpSmap"
new_str1_list = sorted(str1)
print(str1)
print(new_str1_list)
print("".join(new_str1_list))
print(new_str1_list)

# map関数でリスト全てをintにすることはできない。
# list3 = ["1", "2", "3"]
# new_list3 = map(int, list3)
# print(new_list3)
# 実行しても正しい結果が返ってこない。

# 同様に数値から文字にすることはできない。
# list3 = [1, 2, 3]
# new_list3 = map(str, list3)
# print(new_list3)は正しい結果が返ってこない

#　ただし、文字と数値が混じったリストをjoin関数を使って文字列にしたいときはmap関数を使うべき。
list3 = ["a", "vm", 3, 6, 2, 1, "fsf"]
#　print("".join(list3))
# join関数は文字列のみにしか使えないのでエラーが起きる。

new_list3 = map(str, list3)
print("".join(new_list3))
