# *valueでリストを外すことができる
# print(N) => [1, 0] print(*N) => 1 0

H, W = map(int, input().split())
for i in range(H):
    scale = input().split()
    scale = [int(s) for s in scale]
    for j in range(W):
        if scale[j] >= 128:
            scale[j] = 1
        else:
            scale[j] = 0
    print(*scale)
