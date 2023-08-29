def data_types():
    print("Datatype of", x, ":", type(x))
    print("Datatype of", y, ":", type(y))
    print("Datatype of", z, ":", type(z))
    print("Datatype of", a, ":", type(a))
    print("Datatype of", b, ": ", type(b))

    print("Datatype of", list1, ":", type(list1))
    print("Datatype of", tuple1, ":", type(tuple1))
    print("Datatype of", range1, ":", type(range1))
    print("Datatype of", dict1, ":", type(dict1))
    print("Datatype of", set1, ":", type(set1))
    print("Datatype of", list2[0:2], ":", type(list2))


if __name__ == '__main__':
    x = int(input('Enter any integer(ex: 2,42,111) : '))
    y = input('Enter any string(ex: ab,siva,asd) : ')
    z = float((input('Enter any float value (ex: 2.1,0.5,11.12) : ')))
    a = bool(input('Enter boolean value (ex : True,False) :'))
    b = complex(input('Enter Complex numbers (ex: 2+5j) :'))
    list1 = [x, y, z, a, b]
    tuple1 = (x, y, z, a, b)
    range1 = range(10)
    dict1 = {'x': x, 'y': y, 'z': z}
    set1 = {x, y, z}
    list2 = list(tuple1)
    data_types()
