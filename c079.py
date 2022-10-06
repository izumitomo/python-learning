list = input().split()
L = [int(s) for s in list]
count = 0
L2 = [0]

for i in range(L[0]):
    flag = 0
    n = input()
    for j in range(len(L2)):
        if n == L2[j]:
            flag = 1
            break
    if flag == 0:
        L2 += n
        count += 1
    if count == L[1]:
        print(i+1)
        break
if count != L[1]:
    print("unlucky")
