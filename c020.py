from numpy import double


m, p, q = map(double, input().split())
ans = 0

ans = m * (1 - p/100) * (1 - q/100)
print(ans)
