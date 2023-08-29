# Reading the file and capture the data and pass it into function where it required
class VoterList:
    def __init__(self, name, dob_year):
        self.name = name
        self.dob_year = dob_year

    def info(self):
        print(f"Name of the Voter : {self.name}")
        print(f"Birth year of the Voter : {self.dob_year}")


def reading_data_from_file():
    file = open("F:\\data2.txt", 'r')
    list1 = []
    for data in file.readlines():
        for i in data.split():
            list1.append(i)
    file.close()

    print(list1)
    list2 = []
    for i in list1:
        if i.__contains__('-') is True:
            list2.append(i.split('-'))
    print(list2)
    del list2[0]
    print(list2)
    for j in list2:
        obj = VoterList(j[0], j[1])
        obj.info()
        print('-*-' * 20)


if __name__ == '__main__':
    reading_data_from_file()
