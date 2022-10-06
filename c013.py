kirai = input()
N = int(input())
flag = 0
for i in range(N):
    L = input()
    if (kirai in L):
        continue
    print(L)
    flag += 1
if (flag == 0):
    print("none")
