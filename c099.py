import sys

def main(lines):
  numbers = []
  sum = 0
  for i, v in enumerate(lines):
    # print("line[{0}]: {1}".format(i, v))
    if i == 0:
      N, D = map(int, v.split())
    else:
      numbers += [int(v)]
  
  for i in numbers:
    sum += D-i
  ans = D * (D+sum)
  print(ans)
  
if __name__ == '__main__':
  lines = []
  for l in sys.stdin:
    lines.append(l.rstrip('\r\n'))
  main(lines)   
