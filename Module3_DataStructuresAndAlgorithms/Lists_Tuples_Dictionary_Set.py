def list_example():
    length_of_list1 = int(input('Enter the length of the list : '))
    list1 = []
    i = 0
    while True:
        list1_items = input('Enter the items into list : ')
        try:
            if type(int(list1_items)) == int:
                list1.append(int(list1_items))
        except ValueError:
            list1.append(list1_items)

        i += 1
        if length_of_list1 == len(list1):
            break
    print(list1)
    list1.append('siva')
    print(list1)
    del list1[0]
    print(f'List1 : {list1}')
    list2 = ['siva', 2405, 'abhi']
    print(f'List2 :{list2}')
    list3 = list1 + list2
    print(f'Adding List1 and List2 :{list3}')
    print(f'Length of list3 :{len(list3)}')


def tuple_example():
    tuple_ex = ('siva', 'abhi', 2405, 'ram', 2366)
    print(tuple_ex)
    print(f'Length of Tuple :{len(tuple_ex)}')
    print(f'Value of Index {0} of Tuple :{tuple_ex[0]}')
    list4 = list(tuple_ex)
    list4.append('appending to tuple')
    tuple_ex1 = tuple(list4)
    print(tuple_ex1)


def set_example():
    set1 = {1, 1, 3, 's', 's', 'r', 4, 9}
    print(set1)  # set does not accept duplicates
    for items in set1:
        print(items)
    list5 = list(set1)
    del list5[-1]
    set2 = set(list5)
    print(f'Set after deleting last item : {set2}')


def dictionary_example():
    dictionary1 = {'Name': 'Siva', 'Age': 29, 'Id': 2405}
    print(f'Prints all the keys : {dictionary1.keys()}')
    dictionary2 = {'Name': 'ramya', 'Age': 28, 'Id': 2405}
    print(f'Value of the dictionary key : {dictionary2["Name"]}')
    print(f'Value of the dictionary key : {dictionary2.get("Name")}')
    dictionary2["Name"] = "Abhi"
    print(dictionary2)
    print(dictionary2.items())
    if 'Name' in dictionary2:
        print(dictionary2['Name'])
    dictionary2.update({'Id': 2222})
    dictionary2.update({'Dob': '1st Jan 2020'})
    print(dictionary2)
    dictionary2.pop('Dob')
    print(dictionary2)
    dictionary2.popitem()
    print(dictionary2)
    dictionary3 = dict(**{'a': 1, 'b': 2}, **{'c': 3, 'd': 4})
    print(dictionary3)


if __name__ == '__main__':
    list_example()
    tuple_example()
    set_example()
    dictionary_example()
