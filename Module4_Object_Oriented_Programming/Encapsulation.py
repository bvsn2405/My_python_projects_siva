class SuperClass:
    def __init__(self):
        self._value1 = 100  # protected value, we can access the value in same class or in subclass
        self.__value2 = 200  # protected value, we can access the value in only same class

    def fun1(self):
        print(f'The protected Value can be accessed in same class and sub class : {self._value1}')
        print(f'The private Value can be accessed in same class : {self.__value2}')


class SubClass(SuperClass):
    def display(self):
        print(f'The protected Value can be accessed sub classes : {self._value1}')
        try:
            print(f'The private Value can be accessed in same class : {self.__value2}')
        except Exception as e:
            print("Private value can not be accessed in other classes and sub classes. the error is : ", e)


if __name__ == '__main__':
    print('\n')
    print('Calling the SuperClass with object :')
    print('_'*len('Calling the SuperClass with object '))
    print('\n')

    obj1 = SuperClass()
    obj1.fun1()
    print('\n')
    print('Calling the SubClass with object :')
    print('_'*len('Calling the SubClass with object '))
    print('\n')
    obj2 = SubClass()
    obj2.display()
