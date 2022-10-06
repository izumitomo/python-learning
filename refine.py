L =input().split()
list = [int(s) for s in L]

list_n = input()

for i in range(list[0]-1):
    list_n += input()
for i in range(int(len(list_n) / list[2])):
    print(list_n[i*list[2] : (i+1)*list[2]])
print(list_n[int(len(list_n) / list[2]) * list[2]:])
