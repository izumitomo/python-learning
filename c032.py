import sys

price_list = [0, 0, 0, 0]


def main(lines):
    point = 0
    N = int(lines[0])
    for i in range(1, N+1):
        v, p = map(int, lines[i].split())
        price_list[v] += p

    point += int(price_list[0]/100) * 5
    point += int(price_list[1]/100) * 3
    point += int(price_list[2]/100) * 2
    point += int(price_list[3]/100) * 1
    print(point)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
