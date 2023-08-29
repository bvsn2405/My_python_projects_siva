def writing_into_file():
    f = open("F:\\data.txt", 'w')
    f.write('Eligible Voter Id registration list :\n')
    f.write('Name')
    f.write('-')
    f.write('Age')
    f.write('\n')
    f.close()
    f1 = open("F:\\data1.txt", 'w')
    f1.write('Not Eligible Voter Id registration list :\n')
    f1.write('Name')
    f1.write('-')
    f1.write('Age')
    f1.write('\n')
    f1.close()
    while True:
        name = input('Enter your name : ')
        dob_year = int(input('Enter your birth year : '))
        age = 2023 - dob_year

        if age >= 18:
            print('You are eligible for Voter Id registration :')
            f = open("F:\\data.txt", 'a')
            f.write(name)
            f.write('-')
            f.write(str(age))
            f.write('\n')
            f.close()

        else:
            print('You are not eligible for Voter Id registration :')
            f1 = open("F:\\data1.txt", 'a')
            f1.write(name)
            f1.write('-')
            f1.write(str(age))
            f1.write('\n')
            f1.close()

        a = input('Do you want to continue to enter the details (Yes | No)` : ')

        if a == 'no' or a == 'No' or a == 'NO':
            break


def reading_file():
    print("This is the data of file1 :\n")
    f = open("F:\\data.txt")
    print(f.read())
    f.close()
    print('-*-' * 25,'\n')
    print("This is the data of file2 :\n")
    f = open("F:\\data1.txt")
    print(f.read())
    f.close()


if __name__ == '__main__':
    writing_into_file()
    reading_file()