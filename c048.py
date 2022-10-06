# int型にキャストするのはどのタイミングかは分からないが、細かくやる必要はない？（8行目）
# int型のキャストを外してもエラーが起きない -> xの変数の再定義が起きていた。
x, p = map(float, input().split())
total_price = 0

while(x > 0):
    total_price += x
    x = int(x * (100-p)/100)

print(int(total_price))
