n = int(input())
start = 0
end = 0
high = 0
low = 0

start, end, high, low = map(int, input().split())

for i in range(n-1):
    L = input().split()
    list = [int(s) for s in L]
    if high < list[2]:
        high = list[2]
    if low > list[3]:
        low = list[3]
    if i == n-2:
        end = list[1]

print(start, end, high, low)
