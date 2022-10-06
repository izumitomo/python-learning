import sys


def main(lines):
    count = 0
    X = int(lines[0])
    for i in range(1, 365):
        if lines[0] in str(i):
            count += 1
    print(count)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
