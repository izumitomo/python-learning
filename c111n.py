def binary2int(binary):
    int_val, i, n = 0, 0, 0
    while(binary != 0):
        a = binary % 10
        int_val = int_val + a * pow(2, i)
        binary = binary//10
        i += 1
    return int_val


N, M = map(int, input().split())
s = input()
j = 0
k = 0
ans = []
if N % M != 0:
    for i in range(M - N & M):
        s = s + '0'

cnt = int(len(s)/M)
print(cnt)
for i in range(cnt):
    j = i*M
    s_int = int(s[j:j+M])
    s_int = binary2int(s_int)
    k = k ^ s_int

    print(bin(k))

ans = bin(k)
print(ans[2:])
