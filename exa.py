N = int(input())
point = 0
for i in range(N):
    L = input().split()
    list = [int(s) for s in L]
    if list[0] == 3 or list[0]== 13 or list[0]== 23 or list[0]== 30 or list[0]== 31:
        point += int(0.03*list[1])
    elif list[0] == 5 or list[0]== 15 or list[0]==  25: # list[0] == 5 or 15はダメ
        point += int(0.05*list[1])
    else:
        point += int(0.01*list[1])
    print(list[0], point)
print(point)
