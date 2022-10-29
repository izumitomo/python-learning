# L = list(map(int, input().split()))は上手くいく。
# L = [map(int, input().split())]は上手くいかない。

# += による結合と、appnedによる結合の違い！

list = []
a = [1,2]
b = [3,4]

list += a
list += b
print(list)

list = []

list.append(a)
list.append(b)
print(list)
