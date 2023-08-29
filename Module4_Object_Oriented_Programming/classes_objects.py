class Student:
    def __init__(self, name, age, place):
        print('Here are the details :')
        self.name = name
        self.age = age
        self.place = place

    def info(self):
        print(f'My name is : {self.name}')
        print(f'I am {self.age} years old')
        print(f'I was born in {self.place}')

    def siva(self):
        print([self.name, self.age, self.place])


if __name__ == '__main__':
    s1 = Student('Siva', 29, 'AP')
    s1.info()
    s1.siva()
