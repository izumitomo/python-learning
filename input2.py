# リストで受け取って数値に変換！
L = input().split() #splitがないとエラー
num_L = [int(s) for s in L]
print(num_L)
