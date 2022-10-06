import sys


def main(lines):
    list1 = list(map(int, lines[0].split()))
    print(list1)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
