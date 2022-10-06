import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    word_list = list(map(str, lines[0].split()))
    input_len = len(word_list)
    if input_len == 0:
      print(0)
    elif input_len == 1:
      if word_list[0].isalnum():
        print(len(word_list[0]))
      else:
        sys.exit(100)
    elif input_len == 2:
      if word_list[0].isalnum() and word_list[1].isalnum():
        len_1 = len(word_list[0])
        len_2 = len(word_list[1])
        str1 = word_list[0]
        str2 = word_list[1]

        calc_list = [[0 for i in range(len_2+1)] for j in range(len_1+1)]

        for i in range(len_1+1):
          calc_list[i][0] = i
        for j in range(len_2+1):
          calc_list[0][j] = j

        for i in range(1, len_1+1):
          ac = str1[i-1]
          for j in range(1, len_2+1):
            bc = str2[j-1]
            cost = 0 if (ac == bc) else 1
            calc_list[i][j] = min([
              calc_list[i-1][j] + 1,
              calc_list[i][j-1] + 1,
              calc_list[i-1][j-1] + cost
            ])
        print(calc_list[len_1][len_2])
      else:
        sys.exit(100)
    else:
      sys.exit(100)
      



if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
