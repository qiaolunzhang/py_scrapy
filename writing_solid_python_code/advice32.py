def appendtest(newitem, lista = []):
    print(id(lista))
    lista.append(newitem)
    print(id(lista))
    return lista


appendtest(1)
appendtest.func_defaults