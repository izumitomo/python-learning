N, M = map(int, input().split())
A, B, C = map(int, input().split())
count = 0
for i in range(N):
  R = int(input())
  if C * R - (A + B * M) < 0:
    count+= 1
print(count)
