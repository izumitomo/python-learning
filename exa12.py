# 文字のASCII比較はordを利用する！　
# 逆に数値をASCIIに変換するときはchrを使う！
char = input()
if 48 <= ord(char) <= 57:
  print("Number!")
else:
  print("Not number!")
print(chr(48), chr(57))
