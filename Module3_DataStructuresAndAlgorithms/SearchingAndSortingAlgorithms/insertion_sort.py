def insertion_sort(list2):
    for i in range(1, len(list2)):
        value_to_sort = list2[i]
        while list2[i - 1] > value_to_sort and i > 0:
            list2[i], list2[i - 1] = list2[i - 1], list2[i]
            i = i - 1
    return list2


if __name__ == '__main__':
    list1 = [56, 41, 12, 6, 31, 1, 19, 65, 22, 2]
    print(f'The unsorted list is : {list1}')
    print(f'The sorted list is : {insertion_sort(list1)}')
