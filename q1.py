import numpy as np
for loop in range(100):
    N = 1000000
    count = 0
    list = []
    for i in range(N):
        list += [0]
    random_numbers = np.random.randint(1, N, N)

    for i in range(N):
        list[random_numbers[i]] += 1

    for i in list:
        if i == 3:
            count += 1
#    print(N-count)
    f = open('myfileb_6.txt', 'a')
#    f.write(str(N-count) + " ")
    f.write(str(count) + " ")
