# 逆順ループ
list = [1, 2, 3]

for i in range(len(list)-1, -1, -1):
    print(list[i])

for i in range(len(list))[::-1]:
    print(list[i])

# 後者の方が使いやすそう。前者は開始インデックスと終了インデックスがミスりそう。

for i in range(len(list))[:0:-1]:
    print("[:0:-1]", list[i])

# こうなると微妙なので、終了インデックスを指定するなら前者の方が見やすいかもしれない。

for i in list[::-1]:
    print(i)

for i in list[:1:-1]:
    print(i)
#　3

for i in list[:0:-1]:
    print(i)
# 3
# 2
# for文やlistのスライス機能で逆順にするときは開始インデックスと終了インデックスの場所に注意。
# range(3) -> 0,1,2
# range(3, 5) -> 3,4
# range(6,3,-1) -> 6,5,4
# rangeは引数の数によって仕様が決まるので微妙に使いずらい。[::-1]ができない。
#
