import sys


def main(lines):
    # 入力が
    # 1 3 5
    # 4 6 8
    # なら
    # print(lines) -> [["1", "3", "5"], ["4", "6", "8"]]
    # print(int_lines) -> [1, 3, 5], [4, 6, 8]
    int_lines = []
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
