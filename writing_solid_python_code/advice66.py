def fib(n):
    a, b = 1, 1
    while a < n:
        yield a
        a, b = b, a + b


for i, f in enumerate(fib(10)):
    print(f)

f = fib(10)
print(type(f))
print(dir(f))