from Functions_Math import greet, addition, subtraction, multiplication, division


def greet_using_module():
    greet(name)


def adding_using_module():
    print(f'Addition of {a} and {b} is : {addition(a, b)}')


def division_using_module():
    print('Division of ', a, 'by', b, 'is :', division(a, b))
    return 0


def subtraction_using_module():
    print('subtraction of ', b, 'from', a, 'is :', subtraction(a, b))


def multiplication_using_module():
    print('Multiplication of', a, 'and', b, ' is : ', multiplication(a, b))


if __name__ == '__main__':
    name = input('Enter any name : ')
    a = int(input('Enter the 1st number : '))
    b = int(input('Enter the 2nd number : '))
    greet_using_module()
    adding_using_module()
    subtraction_using_module()
    multiplication_using_module()
    division_using_module()
