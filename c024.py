# 文字列比較は==で出来る！
N = int(input())
values = [0, 0]
for i in range(N):
    command = input().split()
    if command[0] == "SET":
        command_value1 = int(command[1]) - 1
        command_value2 = int(command[2])
        values[command_value1] = command_value2
    if command[0] == "ADD":
        values[1] = values[0] + int(command[1])
    if command[0] == "SUB":
        values[1] = values[0] - int(command[1])

print(values[0], values[1])
