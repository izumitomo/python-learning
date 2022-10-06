N = int(input())
high = 200.0
low = 100.0
for i in range(N):
    list = input().split()
    greater_or_less = list.pop(0)
    height = float(list[0])
    if greater_or_less == "le":
        if height < high:
            high = height
    else:
        if low < height:
            low = height

print(low, high)
