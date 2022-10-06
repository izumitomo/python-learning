# int(input().split())はエラーが起こるので、intならmapを使うのがベター
a, b, R = map(int, input().split())
# a, b, R=input().split()は可能。
N = int(input())
for i in range(N):
    x1, y1 = map(int, input().split())
    if ((x1 - a) ** 2 + (y1 - b) ** 2 >= R ** 2):
        print("silent")
    else:
        print("noisy")
