S = input()
S = S.replace('A', '4').replace('E', '3').replace('G', '6').replace(
    'I', '1').replace('O', '0').replace('S', '5').replace('Z', '2')
# S = S.replaceにしないとだめ。S.replace単体だと置換した結果を反映してくれない。
print(S)
