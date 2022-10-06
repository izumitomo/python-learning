Q = int(input())
for i in range(Q):
    count = 0
    N = int(input())
    n = int(N/2)
    for j in range(1, n+1):  # こうやって範囲指定する。ちなみにrange(3,7)だったらJ=3,4,5,6となる。
        if N % j == 0:
            count += j
        print(count)
    if count == N:
        print("perfect")
    elif abs(count - N) == 1:
        print("nearly")
    else:
        print("neither")
