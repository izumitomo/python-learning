# 入力:apple apleをlistとして受け取った時、list[0][0]="a",list[0][1]="p"となる。
# list[1][4]を指定するとエラー発生。
score = 0
N = int(input())
for i in range(N):
    miss = 0
    word = input().split()
    len_word0 = len(word[0])
    len_word1 = len(word[1])
    if abs(len_word0 - len_word1) != 0:
        continue
    if len_word0 > len_word1:
        len_word0 = len_word1
    for j in range(len_word0):
        if word[0][j] != word[1][j]:
            miss += 1
    if miss == 0:
        score += 2
    elif miss == 1:
        score += 1
print(score)
