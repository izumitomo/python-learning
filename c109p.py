N = int(input())
list = []

for i in range(N):
  name = input()
  num = ""
  for char in name:
    if 48 <= ord(char) <= 57:
      num += char
  list.append([name, int(num)])
list.sort(key = lambda x: x[1])
for ans in list:
  print(ans[0])



# 文字列の初期化は””
# 文字列とリストは違う
