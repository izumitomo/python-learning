N = int(input())
point = 0
for i in range(N):
    d, p = input().split()
    p = int(p)
    if ('3' in d):
        point += int(p * 0.03)
        continue
    if ('5' in d):
        point += int(p * 0.05)
        continue
    point += int(p * 0.01)
print(point)
