import sys

def main(lines):
  min = 50
  max = 0
  numbers = []
  N = int(lines.pop(0))
  for line in lines:
    s, f, t = map(int, line.split())
    sum = s + f + 24-t
    if min > sum:
      min = sum
    if max < sum:
      max = sum
  print(min)
  print(max) 
if __name__ == '__main__':
  lines = []
  for l in sys.stdin:
    lines.append(l.rstrip('\r\n'))
  main(lines)   
