def gen(n):
    for i in range(n):
        yield i**2


for i in gen(5):
    print(i, " ", end="")


print('\n**************************************************')


def square(n):
    ls = [i**2 for i in range(n)]
    return ls


for i in square(5):
    print(i, " ", end="")