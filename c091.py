import math
import sys


def main(lines):
    M, N = map(int, lines[0].split())
    for i in range(1, N+1):
        orange = int(lines[i])
        if orange < M + math.ceil(M/2):
            print(M)
        elif orange < int(orange/M) * M + math.ceil(M/2):
            print(int(orange/M) * M)
        else:
            print((int(orange/M)+1) * M)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
