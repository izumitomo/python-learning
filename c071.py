# 地獄。
from cmath import sqrt
import sys

price_list = [0, 0, 0, 0]


def main(lines):
    M, N = map(int, lines[0].split())
    a = 0
    b = 0
    c = 0
    pita = []
    count = 0
    for i in range(1, 10):
        for j in range(1, i):
            a = i**2 - j**2
            b = 2 * i * j
            c = i**2 + j**2
            list = [a, b, c]
            pita += [sorted(list)]
    pita = pita[:20]
    for tri in pita:
        if M > tri[0] and N > tri[1]:
            count += 1
        if N > tri[0] and M > tri[1]:
            count += 1
    print(count)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
