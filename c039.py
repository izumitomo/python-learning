# 足し算だけならいちいち+を読み取る必要はなかった……

ten_count = 0
one_count = 0
list = input()
number = []
sum = 0
for i in list:
    if i == "<":
        ten_count += 1
        continue
    if i == "/":
        one_count += 1
        continue
    if i == "+":
        number += [ten_count*10 + one_count]
        ten_count = 0
        one_count = 0
number += [ten_count*10 + one_count]
for i in number:
    sum += i
print(sum)
