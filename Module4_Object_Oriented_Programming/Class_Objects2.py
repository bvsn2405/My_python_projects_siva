class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.rollNo = roll_no
        self.marks = marks

    def info(self):
        print(f'Student Name : {self.name}')
        print(f'Student Roll Number : {self.rollNo}')
        print(f'Student Marks : {self.marks}')


def students_data():
    studentList = []
    studentList1 = []
    while True:
        name1 = input('Enter the student name : ')
        rollNo1 = int(input('Enter the roll number of the student : '))
        marks1 = int(input('Enter the marks of the student : '))
        s1 = Student(name1, rollNo1, marks1)
        studentList1.append(s1)
        studentList.append([s1.name, s1.rollNo, s1.marks])
        print('Student details Entered successfully ... ')
        ask = input('Do you want to continue ? (Yes | No ) : ')
        if ask == 'no' or ask == 'No' or ask == 'NO':
            break
    print(studentList)

    for students in studentList1:
        students.info()
        print('-' * 50)


if __name__ == '__main__':
    students_data()
