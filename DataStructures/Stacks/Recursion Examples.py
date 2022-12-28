def fac(n):
    if n == 1:
        return 1  # base case
    else:
        return n * fac(n-1)


print(fac(4))



def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-1)

print(fib(4))
