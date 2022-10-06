N = list(input())
while(1):
    n = int(''.join(N))
    flag = 0
    length = len(N)
    for i in range(int(length / 2)):
        swap = N[i]
        N[i] = N[-i-1]
        N[-i-1] = swap
    m = ''.join(N)
    num = int(m) + n
    numstr = list(str(num))
    for i in range(int(length / 2)):
        if numstr[i] != numstr[-i-1]:
            flag = -1
            break
        flag += 1
    if flag == int(length / 2):
        break
    N = list(str(num))
print(num)
    
    
