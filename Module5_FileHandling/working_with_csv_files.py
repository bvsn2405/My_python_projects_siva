# Reading data from the csv file

import csv


class Users:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def info(self):
        print(f'Username is : {self.name}')
        print(f'Email address of the user is : {self.email}')


def reading_from_csv_file():
    with open("F:\\data.csv") as csv_file:
        data_file = csv.reader(csv_file)
        next(data_file)
        for row in data_file:
            user_details = Users(row[0], row[1])
            user_details.info()
            print('_' * 50)


if __name__ == '__main__':
    print('\n')
    reading_from_csv_file()
