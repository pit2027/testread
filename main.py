def get_list():
    for x in [1,3,5,7]:
        yield x




if __name__ == '__main__':

    a = get_list()
    #print(next(a))
    #print(next(a))
    #print(next(a))
    #print(next(a))
    for x in a:
        print(x)
    #b = get_list()
    print(list(a))

#Функцию генератор можно перебираать только один раз