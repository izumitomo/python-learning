from cmath import sqrt


xc, yc, r1, r2 = map(int, input().split())
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    distance = (x-xc)**2 + (y-yc)**2
    if r1**2 <= distance and distance <= r2**2:
        print("yes")
    else:
        print("no")
