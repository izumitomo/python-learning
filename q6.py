# int型のiで
# if i/100 == 1:
# i/100はfloat型になっているので、int型にキャストしなければならない。逆に
# if i/100 > 1:
# ならばいちいちfloat型に明示的にキャストする必要はない。(おそらくjavaなどではfloat(i/100)にしないとエラーが起こる。)


ans = 0
data = 0
for i in range(999, 9, -1):
    data = i
    count = 0
    if int(i/100) == 9:
        count += 2
        i = i % 100
    if float(i/500) >= 1:
        count += 1
        i = i % 500
        #print(data, i, count)
    if float(i/100) >= 1:
        if int(i/100) == 4:
            count += 2
        else:
            count += int(i/100)
        i = i % 100
        #print(data, i, count)
    if int(i/10) == 9:
        count += 2
        i = i % 10

    if float(i/50) > 1:
        count += int(i/50)
        i = i % 50
        #print(data, i, count)
    if float(i/10) >= 1:
        if int(i/10) == 4:
            count += 2
        else:
            count += int(i/10)
        i = i % 10
        #print(data, i, count)
    if i == 9:
        count += 2
        i = 0
    if float(i/5) >= 1:
        count += int(i/5)
        i = i % 5
        #print(data, i, count)
    if i >= 1:
        if i == 4:
            count += 2
        else:
            count += i
        #print(data, i, count)
    if count == 10:
        ans += data
        print(data)
print(ans)
