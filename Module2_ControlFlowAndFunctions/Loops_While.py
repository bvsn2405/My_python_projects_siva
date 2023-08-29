def multi_table():
    i = 1
    while i < 11:
        print(i, ' x ', a, ' = ', i * a)
        i += 1


if __name__ == '__main__':
    a = int(input('Enter the number for which you want multiplication table  : '))
    multi_table()
