m, d = input().split()
len_m = len(m)
len_d = len(d)
flag = 0
for i in m:
  if m[0]!= i:
    flag = 1
    break

for i in d:
  if m[0]!= i:
    flag = 1
    break

if flag == 0:
  print("Yes")
else:
  print("No")




