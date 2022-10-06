# 配列中の探索には a in listを使う。
L = input().split()
ans_numbers = [int(s) for s in L]
N = int(input())
for i in range(N):
    count = 0
    numbers = input().split()
    numbers = [int(s) for s in numbers]
    for j in range(6):
        # if numbers[j] == ans_numbers[0] or numbers[j] == ans_numbers[1] or numbers[j] == ans_numbers[2] or numbers[j] == ans_numbers[3] or numbers[j] == ans_numbers[4] or numbers[j] == ans_numbers[5]:
        if numbers[j] in ans_numbers:
            count += 1
    print(count)
