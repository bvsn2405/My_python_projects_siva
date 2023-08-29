def linear_search(list1, search_element):
    index = 0
    found = False
    while index < len(list1):
        if list1[index] == search_element:
            print(f'Element Found at index :{index}')
            found = True
            break
        else:
            index += 1
    if not found:
        print('Element not found !')


if __name__ == '__main__':
    list2 = [2, 23, 1, 35, 7, 3, 6, 1, 12, 6, 2, 23]
    search_element1 = 35
    linear_search(list2, search_element1)
