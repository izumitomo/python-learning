list = input().split()
L = [int(s) for s in list]
syo = []
max = 0
for i in range(L[0]):
    num = int(input())
    syo.append(int(num / L[1]))
    if max < num:
        max = num

masu = int(max / L[1])

for j in range(L[0]):
    all = []
    for i in range(masu):
        if syo[j] > 0:
            all += '*'
            syo[j] -= 1
        else:
            all += '.'
    print(str(j+1) + ':' + ''.join(all))

