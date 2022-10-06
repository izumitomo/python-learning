kirai = input()
N = int(input())
flag = 0
for i in range(N):
    L = input()
    if (kirai in L):  # 文字列比較はこれが一番楽。
        continue
    print(L)
    flag += 1
    # pythonはi++が使えない.
if (flag == 0):
    print("none")
