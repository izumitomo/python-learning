# 小数点切り上げにはmath.ceilを使う！
import math


Max = int(input())
N = int(input())

paper = 0
count = 0

list1 = input().split()
hour = int(list1[0])
paper = int(list1[2])

for i in range(N-1):
    x, y, c = map(int, input().split())
    paper += c
    if hour != x:
        hour = x
        paper -= c
        count += math.ceil(paper/Max)
        paper = c

count += math.ceil(paper/Max)
print(count)
