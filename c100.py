import sys


def main(lines):
    N, M, S = map(int, lines[0].split())
    length_list = []
    time = 0
    count = 0
    for i in range(1, N+1):
        m, s = map(int, lines[i].split())
        length_list += [m*60 + s]
    sort_length_list = sorted(length_list)
    for length in sort_length_list:
        time += length
        if time > M*60 + S:
            break
        count += 1
    print(count)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
