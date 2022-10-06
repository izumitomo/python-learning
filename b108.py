import sys

def main(lines):
  space = []
  people = []
  gondra, group = map(int, lines.pop(0).split())
  ans = [0] * gondra
  for i in range(gondra):
    space += [int(lines.pop(0))]
  for i in range(group):
    people += [int(lines.pop(0))]
  
  i = 0
  gondra_id = 0
  while(1):
    if people[i] <= space[gondra_id]:
      ans[gondra_id] += people[i]
      i += 1   
    else:
      people[i] -= space[gondra_id]
      ans[gondra_id] += space[gondra_id]
    if gondra_id == gondra-1:
      gondra_id = 0
    else:
      gondra_id += 1
    
    if i == group:
      break
  
  for i in range(gondra):
    print(ans[i])

if __name__ == '__main__':
  lines = []
  for l in sys.stdin:
    lines.append(l.rstrip('\r\n'))
  main(lines)   
