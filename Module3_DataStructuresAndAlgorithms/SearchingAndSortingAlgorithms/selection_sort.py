def selection_sort(list1):
    for i in range(len(list1) - 1):
        min_val = min(list1[i:])
        min_index = list1.index(min_val, i)
        list1[i], list1[min_index] = list1[min_index], list1[i]
    print(f'List after sorting: {list1}')


def selection_sort2(list3):
    i = 0
    for i in range(len(list3) - 1):
        min_val = list3[i]
        min_index = i
        for j in range(i + 1, len(list3) - 1):
            if list3[j] < list3[i]:
                j = min_index
    print("This sort done by 2nd program :", list3)


if __name__ == '__main__':
    list2 = [2, 23, 1, 35, 7, 3, 6, 1, 12, 6, 2, 23, 87]
    print(f'List before sorting: {list2}')
    selection_sort(list2)
    selection_sort2(list2)
