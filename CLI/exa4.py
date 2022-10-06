import sys


def main(lines):
    # 入力が
    # 1 3 5
    # 4 6 8
    # なら
    # print(lines) -> [["1", "3", "5"], ["4", "6", "8"]]
    # print(int_lines) -> [1, 3, 5], [4, 6, 8]
    # ちなみにsplit()は空白を削除して文字列->リストにする。
    # strip()はデフォルトで開業を削除する。
    int_lines = []
    print(lines)
    for line in lines:
        int_list = [int(s) for s in line]
        print(int_list)
        int_lines += [int_list]
    print(int_lines)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        l = l.strip("\n")
        l_list = l.split()
        lines.append(l_list)
    main(lines)
