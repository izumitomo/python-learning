import sys


def main(lines):
    # 入力が
    # N
    # 4 6 8
    # 1 2 3
    # のパターンの解き方。
    N = lines.pop(0)
    # これをした時点で、for line in lines
    #
    #
    #
    #

    print(lines)
    for line in lines:
        l_list = line.split()
        print(l_list)
        int_list = [int(s) for s in l_list]
        print(int_list)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip("\n"))
    main(lines)
