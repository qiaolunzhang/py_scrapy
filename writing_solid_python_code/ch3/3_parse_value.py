def inc(n):
    print(id(n))
    n = n + 1
    print(id(n))


n = 3
print(id(n))
print('*************************')

inc(n)

print('*************************')
print(id(n))


print('*************************')


def change_list(orginator_list):
    print("orginator list is:", orginator_list)
    new_list = orginator_list
    new_list.append("I am new")
    print("new list is:", new_list)
    return new_list


orginator_list = ['a', 'b', 'c']
new_list = change_list(orginator_list)
print(new_list)
print(orginator_list)



print('*************************')
print('*************************')


def change_me(org_list):
    print(id(org_list))
    new_list = org_list
    print(id(new_list))
    if len(new_list) > 5:
        new_list = ['a', 'b', 'c']
    for i, e in enumerate(new_list):
        if isinstance(e, list):
            new_list[i] = "***"
    print(new_list)
    print(id(new_list))

test1 = [1, ['a', 1, 3], [2, 1], 6]
change_me(test1)
print(test1)

test2 = [1, 2, 3, 4, 5, 6, [1]]
change_me(test2)
print(test2)
