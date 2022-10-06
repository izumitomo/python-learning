from re import A


seven_point = 0
pre_seven_point = 0
daily_point = 1
total_point = 0
n = 1000000000
a = 1
b = 1
length = 0
start_search = 0

for lemgth in range(13):
    pre_seven_point = seven_point
    seven_point = 0

    for j in range(i):
        seven_point += b * 9**j * 10**(i-j-1)
    sum = a * 10**(length-1) + seven_point
    if sum > n:
        pre_daily_point = a * 10**(length-2)
        break

for i in range(0, 7):
    pre_sum = sum
    sum = pre_seven_point * i + pre_daily_point + a * 10**(length-3) * i
    if sum > n:
        day = 10**(length-2) + 10**(length-3) * i-1
        total_point = pre_sum
        break
    if i == 6:

        for j in range(9, 7, -1):
            # pre_seven_point =
            pre_sum = sum
            sum = pre_seven_point * j + \
                pre_daily_point + a * 10**(length-3) * j
            if sum < n:
                day = 10**(length-2) + 10**(length-3) * j-1
                total_point = pre_sum
                break

while (total_point < n):
    day += 1
    total_point += a
    if 7 in str(day):
        total_point += b

print(day)
