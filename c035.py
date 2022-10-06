# 要素を取り出して削除するのはpop
# list_0 = list.pop(0)で先頭要素が無くなる。
# pop(-1)で最後の要素を取り出せる

N = int(input())
count = 0
for i in range(N):
    score = input().split()
    type = score.pop(0)
    score = [int(s) for s in score]
    sum = 0
    for j in score:
        sum += j
    if sum < 350:
        continue

    if type == "l":
        if score[3] + score[4] < 160:
            continue
    else:
        if score[1] + score[2] < 160:
            continue
    count += 1
print(count)
