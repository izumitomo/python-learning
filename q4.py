
count = 0

for i in range(10, 1000000):
    for j in range(3):
        tmp = 1
        list = []
        str_i = str(i)
        len_i = len(str_i)
        for k in str_i:
            list += [int(k)]
        for l in list:
            tmp *= l
        if tmp < 10:
            if j == 2:
                count += 1
            else:
                break
        i = tmp


""" count = 0
for i in range(10, 1000000):
    for j in range(3):
        list = []
        second_i = 1
        str_i = str(i)
        len_i = len(str_i) - 1
        #print(str_i, len_i)
        while len_i >= 0:
            list += [int(i/10**len_i)]
            i -= int(i/10**len_i) * 10**len_i
            len_i -= 1
        #print(list, len_i, second_i)
        for k in list:
            second_i *= k
        #print(list, len_i, second_i, j)
        if second_i < 10:
            if j == 2:
                count += 1
            else:
                break
        else:
            i = second_i
 """

print(count)


""" count = 0
for i in range(10, 1000000):
    list = []
    second_i = 1
    str_i = str(i)
    len_i = len(str_i) - 1
    #print(str_i, len_i)
    while len_i >= 0:
        list += [int(i/10**len_i)]
        i -= int(i/10**len_i) * 10**len_i
        len_i -= 1
    #print(list, len_i)
    for j in list:
        second_i *= j
    if second_i < 10:
        continue
    else:
        i = second_i

    second_i = 1
    list = []
    str_i = str(i)
    len_i = len(str_i) - 1
    # print(i)
    while len_i >= 0:
        list += [int(i/10**len_i)]
        i -= int(i/10**len_i) * 10**len_i
        len_i -= 1
    #print(list, len_i)
    for j in list:
        second_i *= j
    if second_i < 10:
        continue
    else:
        i = second_i

    second_i = 1
    list = []
    str_i = str(i)
    len_i = len(str_i) - 1
    # print(i)
    while len_i >= 0:
        list += [int(i/10**len_i)]
        i -= int(i/10**len_i) * 10**len_i
        len_i -= 1
    for j in list:
        second_i *= j
    if second_i < 10:
        count += 1
    else:
        continue
print(count)
 """
