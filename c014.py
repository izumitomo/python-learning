n, r = map(int, input().split())
r = r * 2
for i in range(n):
    h, w, d = map(int, input().split())
    if (h >= r and w >= r and d >= r):  # pythonは&& ||を使わずにand orを使う
        print(i + 1)
