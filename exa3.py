N = int(input())
all = []
for i in range(N):
    list = input().split()
    L = [int(s) for s in list]
    all.append(L) # += Lだとリストの中にリストを作れない。
# [[1,2,3],[1,2,3]]ではなく、[1,2,3,1,2,3]となる。

swap = []
for i in range(N):
    for j in range(i, N):
        if all[i][0] < all[j][0]:
            swap = all[i]
            all[i] = all[j]
            all[j] = swap
        elif all[i][0] == all[j][0]:
            if all[i][1] < all[j][1]:
                swap = all[i]
                all[i] = all[j]
                all[j] = swap
            elif all[i][1] == all[j][1]:
                if all[i][2] < all[j][2]:
                    swap = all[i]
                    all[i] = all[j]
                    all[j] = swap

for i in all:
    print(*i)
