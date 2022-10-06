import sys


def main(lines):
    stare = 1
    count = 0
    n = int(lines[0])
    for line in lines[1::]:
        count += abs(int(line) - stare)
        stare = int(line)
    print(count)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
