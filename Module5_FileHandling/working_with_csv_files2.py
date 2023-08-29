import csv


def writing_data_into_csv_file():
    with open("F:\\data1.csv", 'w') as csv_file:
        data_file = csv.writer(csv_file, delimiter=';')
        while True:
            list_row = []
            name = input('Enter name : ')
            id_no = input('Enter Id: ')
            email = input('Enter Email :')
            list_row.append(name)
            list_row.append(id_no)
            list_row.append(email)
            data_file.writerow(list_row)
            ask = input('Press Enter key to continue or enter no to stop :')
            if ask == 'no' or ask == 'NO' or ask == 'No':
                break


# it prints the data from csv file into dictionary form
def print_data_into_dictionary_form():
    with open("F:\\data1.csv") as read_csv:
        data_csv = csv.DictReader(read_csv)
        for rows in data_csv:
            print(rows)


if __name__ == '__main__':
    writing_data_into_csv_file()
    print_data_into_dictionary_form()
