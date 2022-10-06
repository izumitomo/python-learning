import sys


def main(lines):

    N, K, P = map(int, lines[0].split())
    words = lines[1].split()
    sorted_words = sorted(words)
    if K*P-1 <= len(sorted_words):
        for i in range(K*(P-1), K*P):
            print(sorted_words[i])
    else:
        for i in sorted_words[K*(P-1)::]:
            print(i)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
