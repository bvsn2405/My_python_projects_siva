# Arithmetic Operators
def addition():
    print(f'Addition of {a} , {b} is {a + b}')  # addition


def subtraction():
    print(f'Subtraction of {b} from {a} is {a - b}')


def multiplication():
    print(f'Multiplication of {a} * {b} is {a * b}')


def division():
    print(f'Division of {a} by {b} is {a / b}')


def floor_division():
    print(f'Floor division of {a} / {b} is {a // b}')


def remainder():
    print(f'Reminder of {a} by {b} is {a % b}')


def exponent():
    print(f'Exponent of {a} by {b} is {a ** b}')


# Logical Operators
def operators():
    print(not a == b)  # prints True or False based on the condition
    print(1 and 3)  # evaluate the last  value
    print(1 or 3)  # evaluate the true value
    print(5 and 0)  # evaluate the last value
    print(0 or 10)  # evaluate the true value
    print(a < b)  # Comparison operator - prints boolean value
    print(a > b)  # Comparison operator - prints boolean value
    print(a == b)  # Comparison operator - prints boolean value


if __name__ == '__main__':
    a = int(input("Enter 1st number : "))
    b = int(input("Enter 2nd number : "))
    addition()
    subtraction()
    multiplication()
    division()
    exponent()
    floor_division()
    remainder()
    operators()
