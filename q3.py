f = open('myfileb_6.txt', 'r')
sum = 0
data = f.read()
list1 = list(map(int, data.split()))
for i in list1:
    sum += i
print(sum / len(list1))
