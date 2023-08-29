def factorial_program(num1):
    if num1 == 0 or num1 == 1:
        return 1
    else:
        return num1 * factorial_program(num1 - 1)


def fibonacci_series():
    print("Fibonacci series without recursion : ")
    n_terms = int(input('Enter how many terms you need to print the fibonacci series :'))
    n1 = 0
    n2 = 1
    count = 0
    fibonacci_series_list = []
    if n_terms <= 0:
        print('Please enter only positive integer')
    elif n_terms == 1:
        print(n1)
    else:
        print('Fibonacci series : ')
        while count < n_terms:
            n3 = n1 + n2
            print(n1)
            fibonacci_series_list.append(n1)
            n1 = n2
            n2 = n3
            count += 1
    print(fibonacci_series_list)

    # Python program to display the Fibonacci sequence


def recursion_fibo_series(x):
    if x <= 1:
        return x
    else:
        return recursion_fibo_series(x - 1) + recursion_fibo_series(x - 2)


num2 = int(input('Enter the number for factorial : '))


def febo_series_recursion():
    print('Fibonacci series using Recursion')
    y = int(input('Enter how many terms you need to print the fibonacci series :'))

    if y <= 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(y):
            print(recursion_fibo_series(i))


if __name__ == '__main__':
    print(f'The factorial of {num2} is {factorial_program(num2)}')
    fibonacci_series()
    febo_series_recursion()
