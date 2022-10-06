import sys


def main(lines):
    n_k = lines.pop(0)
    k = int(n_k.split()[1])
    print(k)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
