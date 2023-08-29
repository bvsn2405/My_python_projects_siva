def math_operates():
    a = int(input('Enter 1st number : '))
    b = int(input('Enter 2nd number : '))
    add = lambda num1, num2: num1 + num2
    mul = lambda num1, num2: num1 * num2
    print('Adding with Lambda function :', add(a, b))
    print('Multiplication with Lambda function :', mul(a, b))


def palindrome1():
    palindrome = lambda string1: string1[::-1]
    # print(palindrome)
    if string == palindrome(string):
        print(f"\'{string}\' is  palindrome")
    else:
        print(f"\'{string}\' is not palindrome")


if __name__ == '__main__':
    string = input('Enter string : ')
    palindrome1()
    math_operates()
