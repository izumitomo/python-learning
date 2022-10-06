# 文字列の先頭消去はpopではできない。popはリスト型のみでstr型は無理というエラーが出る。
# そのため、先頭を消去した文字列を代入するしかない。
# list=list[1::]

# if文の条件式をandで繋げると、前から順番に実行し、flaseの場合はand以降の条件式を実行しない。
# 17行目のand文を入れ替えると空の配列にアクセスしてエラーが起こる。
import sys


def main(lines):
    N, A, B = map(int, lines[0].split())
    schedule_list = lines[1]
    belt_a_list = lines[2]
    belt_b_list = lines[3]
    for i in range(N):
        schedule = schedule_list[0]
        if len(belt_a_list) > 0 and schedule == belt_a_list[0]:
            belt_a_list = belt_a_list[1::]
        if len(belt_b_list) > 0 and schedule == belt_b_list[0]:
            belt_b_list = belt_b_list[1::]
        schedule_list = schedule_list[1::]
    print(len(belt_a_list), len(belt_b_list))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
