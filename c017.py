A, B = map(int, input().split())
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if A > a:
        print("High")
    elif A < a:
        print("Low")
    else:
        if B > b:
            print("Low")
        else:
            print("High")
