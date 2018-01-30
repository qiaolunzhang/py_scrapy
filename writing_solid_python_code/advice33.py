def SumFun(*args):
    result = 0
    for x in args[0:]:
        result += x
    return result


print(SumFun(2, 4))
print(SumFun(1, 2, 3, 4, 5))
print(SumFun())


def category_table(**kwargs):
    for name, value in kwargs.items():
        print('{0} is a kind of {1}'.format(name, value))


category_table(apple = 'fruit', carrot = 'vegetable', Python = 'programming language')
category_table(BMW = 'Car')


def set_axis(x, y, xlabel='x', ylabel='y', *args, **kwargs):
    print(x)
    print(y)
    for i in args[0:]:
        print(i)


set_axis(2, 3, "test1", "test2", "test3", my_kwarg="test3")
set_axis(2, 3, my_kwarg="test3")
