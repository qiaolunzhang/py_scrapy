# 下面的代码运行没问题，但是不简洁
words = ['   Are', '   abandon', 'Passion', 'Business', ' fRuit   ', 'quit']
size = len(words)
newlist = []
for i in range(size):
    print(words[i].strip())
    if words[i].strip().istitle():
        newlist.append(words[i])
print(newlist)
print('*****************************************************')

# 使用列表解析
nested_list = [['Hello', 'World'], ['Goodbye', 'World']]
nested_list = [[s.upper() for s in xs] for xs in nested_list]
print(nested_list)
print('*****************************************************')

# 支持多重迭代，相当于笛卡尔积
test = [(a, b) for a in ['a', '1', 1, 2] for b in ['1', 3, 4, 'b'] if a != b]
print(len(test))


# 列表解析中语法的表达式可以是简单表达式，也可以是复杂表达式
def f(v):
    if v%2 == 0:
        v = v**2
    else:
        v = v + 1
    return v


expression = [f(v) for v in  [2, 3, 4, -1] if v>0]
print(expression)

expression = [v**2 if v%2 == 0 else v+1 for v in [2, 3, 4, -1] if v > 0]
print(expression)


fh = open("test.txt", "r", encoding='utf-8')
#result = [i for i in fh if "en" in i]
#print(result)
result = [i for i in fh]
print(len(result))