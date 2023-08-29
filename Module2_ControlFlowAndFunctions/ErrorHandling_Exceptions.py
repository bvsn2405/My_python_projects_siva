def print_index():
    try:
        i = int(input('Enter the index to print the number :'))
        return li[i]
    except ValueError as e:
        return f'Entered wrong key and the error is : {e}'
    except IndexError as e:
        return f'Entered index out of range and the error is : {e}'
    finally:
        print(li)
        print('Length of the list is : ', len(li))


if __name__ == '__main__':
    li = [32, 6, 2, 7, 80, 23]
    print(print_index())
