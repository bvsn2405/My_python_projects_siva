class Error(Exception):
    pass


class DobException(Error):
    pass


def apply_exam():
    try:
        year = int(input('Enter birth year : '))
        age = 2023 - year
        try:
            if 30 > age > 20:
                print('You are eligible for the exam you can apply for the exam ..')
            else:
                raise DobException

        except DobException:
            print('You are not eligible for the exam you can not apply for the exam ..')
    except ValueError as ex:
        print('You are not entered an integer.Please Enter Valid DOB year ..', ex)
    finally:
        print('The Execution is done for the finally block..!')


if __name__ == '__main__':
    apply_exam()
