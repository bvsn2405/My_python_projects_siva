def variables():
    a = 5  # variable int type
    print(type(a))
    b = "Siva"  # variable string type
    print(type(b))
    c = str(a)  # a int variable converts into string variable
    print(type(c))
    d = 2.5  # variable float type
    print(type(d))
    print('\n******************************************************************\n')
    print('Python is case sensitive')
    print('------------------------\n\n')
    print(f'Variable1_ siva :{siva}')
    print(f'Variable2_ Siva :{Siva}')
    print(f'Variable3_ SIVA :{SIVA}')
    print(f'Variable4_ sIVA :{sIVA}')
    print(f'Variable5_ sivA :{sivA}')


if __name__ == '__main__':
    siva = 5
    Siva = 'abc'
    SIVA = 2.5
    sIVA = 2 + 2j
    sivA = "Siva"
    variables()
