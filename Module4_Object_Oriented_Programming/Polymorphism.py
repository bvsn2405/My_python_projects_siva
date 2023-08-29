from multipledispatch import dispatch


# Method overloading polymorphism

class PolyExample1:
    @dispatch(int, int)
    def add(self, num1, num2):
        print(f'Sum of two integers: {num1 + num2}')

    @dispatch(int, int, int)
    def add(self, num1, num2, num3):
        print(f'Sum of three integers: {num1 + num2 + num3}')

    @dispatch(str, str)
    def add(self, str1, str2):
        print(f'Concatenation of two strings : {str1 + str2}')


# this is another example of method overloading

class PolyExample2:
    @staticmethod
    def method_overload_ex(a=None, b=None):
        if a is None and b is None:
            print('This is the example of Polymorphism')
        elif a is not None and b is None:
            if type(a) == int or type(a) == float:
                print(f'The number is : {a}')
                fact = 1
                if type(a) is int:
                    for i in range(1, a + 1):
                        fact = fact * i
                    print(f'The factorial of {a} is {fact}')
            else:
                print(f'The entered string : {a}')
                a1 = a[::-1]
                if a == a1:
                    print(f'The entered string {a} is a palindrome !')
                else:
                    print(f'The entered string {a} is a not palindrome..')
        else:
            if type(a) == int and type(b) == int:
                print(f'The sum of {a},{b} is : {a + b}')
            elif type(a) == str and type(b) == str:
                print(f'The Concatenation of {a},{b} is : {a + b}')
            else:
                print(f'The type {a} is {type(a)}')
                print(f'The type {b} is {type(b)}')


# Method override polymorphism

class A:
    def override_ex(self):
        print('The method is from Class A !')


class B(A):
    def override_ex(self):
        print('The method is from Class B !')
        print('it is overriding the method from parent class A !')


# This is an example of Operator Overload
class OperatorOverload:
    def __init__(self, num1):
        self.num1 = num1

    def __add__(self, second):
        return self.num1 + second.num1

    def __mul__(self, other):
        return self.num1 * other.num1

    def __sub__(self, other):
        return self.num1 - other.num1

    def __gt__(self, other):
        return self.num1 > other.num1


if __name__ == '__main__':
    print('\n')
    print('This is an example of method overloading polymorphism :')
    print('-'*len('This is an example of method overloading polymorphism :\n'))

    obj1 = PolyExample1()
    obj1.add(10, 20)
    obj1.add(10, 20, 30)
    obj1.add('Hello ', 'Abhi')
    print('\n', '*' * 60, '\n')
    print('This is another example of method overloading polymorphism :')
    print('-'*len('This is another example of method overloading polymorphism :\n'))

    obj = PolyExample2()
    obj.method_overload_ex()
    obj.method_overload_ex(5.5)
    obj.method_overload_ex(5)
    obj.method_overload_ex('asa')
    obj.method_overload_ex('siva')
    obj.method_overload_ex(2, 3)
    obj.method_overload_ex("Hello ", "World !")
    obj.method_overload_ex(2, 'siva')
    print('\n', '*' * 60, '\n')
    print('This is an example of method overriding polymorphism :')
    print('-'*len('This is an example of method overriding polymorphism :\n'))

    obj2 = A()
    obj2.override_ex()
    obj3 = B()
    obj3.override_ex()
    print('\n', '*' * 60, '\n')
    print('This is example of operator overloading polymorphism :')
    print('-'*len('This is example of operator overloading polymorphism :\n'))

    oper_overload1 = OperatorOverload(2)
    oper_overload2 = OperatorOverload(3)
    print(f'This is Addition function of operator overload  polymorphism : {oper_overload1 + oper_overload2}')
    print(f'This is Multiplication function of operator overload polymorphism : {oper_overload1 * oper_overload2}')
    print(f'This is Subtraction function of operator overload polymorphism : {oper_overload1 - oper_overload2}')
    print(f'This is Greater than function of operator overload polymorphism : {oper_overload1 > oper_overload2}')
