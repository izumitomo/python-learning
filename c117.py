import sys

def main(lines):
  count = 0
  N, M = map(int, lines.pop(0).split())
  shop_info = list(map(int, lines.pop(0).split()))
  for i in range(N):
    balance = shop_info[2] * int(lines[i]) - M * shop_info[1] - shop_info[0]
    if balance < 0:
      count += 1 
  
  print(count)
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
