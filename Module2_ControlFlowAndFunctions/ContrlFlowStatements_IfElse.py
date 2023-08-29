def math_operations():
    math_operator = input('Enter the math operation(add/sub/mul/div) :')
    if math_operator == 'add':
        print(f"Addition of {a}, {b} is: {a + b}")
    elif math_operator == 'sub':
        print(f"Subtraction of {a} from {b} is: {b - a}")
    elif math_operator == 'mul':
        print(f"Multiplication of {a}, {b} is: {a * b}")
    elif math_operator == 'div':
        print(f"Division of {a} by {b}:\nQuotient is: {a // b}\nRemainder is: {a % b}")
    else:
        print('Please enter valid Math operation ! ')


if __name__ == '__main__':
    a = int(input('Enter the 1st Number : '))
    b = int(input('Enter the 2nd number : '))
    print('Note : \"add for Addition\" , \"sub for Subtraction\" , \"mul for Multiplication\" , \"div for Division\" ')
    math_operations()
