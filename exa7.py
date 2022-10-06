N = list("12345")
print(N)
print(*N)
length = len(N)
N1 = ''.join(N)
N2 = ",".join(N)
print(length, N1, N2)
# スマートな要素の入れ替え　数値でも可.
for i in range(int(length/2)):
    N[i], N[-i-1] = N[-i-1], N[i]
print(N)
# more smart
N3 = N[::-1]
print(N3)
# 絶対こっちの方が楽！　下でも行うが1文字毎に区切っていないリストでもこれで対応できる！

# ちなみに 数値ならこれで入れ替え可能
a = 1
b = 2
a, b = b, a
print(a, b)

# 文字列で試す。
word = ["apple", "banana"]
word[0], word[1] = word[1], word[0]
print(word)
# 出来た！！


# さらにスマートな要素の逆順取得
N0 = list(reversed(N))
print(N0)

N = '12345'
print(N)
print(N[2], N[3], N[4])
# reversedで文字列を逆順にするには一旦、リスト構造に変換してから、逆順にして、連結するという流れが必要になる。
N0 = list(reversed(N))
print(N0)
N0 = "".join(N0)
print(N0)

# ちなみにこっちだと簡単。
new_N = N[::-1]
print(new_N)
