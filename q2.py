def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    if n == 2:
        return 5
    else:
        return fib(n-1) + fib(n-2) + fib(n-3)


print(fib(27))
