import sys


def main(lines):
    # 入力が
    # 1
    # 4
    # 5
    # なら
    # print(lines) -> ["1", "4", "5"]
    # print(int_list) -> [1, 4, 5]

    print(lines)
    int_list = [int(s) for s in lines]
    print(int_list)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
