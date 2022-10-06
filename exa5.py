N = int(input())
L = []
n = 0
len1 = 0
for i in range(N):
    num =input()
    n0 = (int(num, 2))#文字列の2進数を受け取って10進数表記
    n ^= n0
leng = len(num)
len0 = len(bin(n)[2:])# bin(n)だと0bが付いてくる
len1 = leng - len(bin(n)[2:])
for i in range(len1):
    print("0", end = '')
print(bin(n)[2:])