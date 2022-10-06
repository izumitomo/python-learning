list = input().split()

if list[4] == "x":
    if list[1] == "+":
        ans = int(list[0]) + int(list[2])
    else:
        ans = int(list[0]) - int(list[2])
elif list[2] == "x":
    if list[1] == "+":
        ans = int(list[4]) - int(list[0])
    else:
        ans = int(list[0]) - int(list[4])
else:
    if list[1] == "+":
        ans = int(list[4]) - int(list[2])
    else:
        ans = int(list[4]) + int(list[2])
print(ans)
