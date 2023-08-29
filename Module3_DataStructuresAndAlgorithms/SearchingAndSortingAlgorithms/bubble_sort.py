def bubble_sort(list1):
    for i in range(len(list1) - 1):
        for j in range(len(list1) - 1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    print(f"The sorted list is : {list1}")


if __name__ == '__main__':
    list2 = [2, 23, 1, 35, 7, 3, 6, 1, 12, 6, 2, 23]
    print(f"The unsorted list is : {list2}")
    bubble_sort(list2)
