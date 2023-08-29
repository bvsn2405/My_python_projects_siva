def pivot_place(first, last):
    pivot = list1[first]
    left = first + 1
    right = last
    while True:
        while left <= right and list1[left] <= pivot:
            left += 1
        while left <= right and list1[right] >= pivot:
            right -= 1
        if right < left:
            break
        else:
            list1[left], list1[right] = list1[right], list1[left]
    list1[first], list1[right] = list1[right], list1[first]
    return right


def quick_sort(list5, first, last):
    if first < last:
        p = pivot_place(first, last)
        quick_sort(list5, first, p - 1)
        quick_sort(list5, p + 1, last)


def quick_sorting_method2(list3):
    if len(list3) <= 1:
        return list3
    else:
        pivot = list3.pop()
    list3_lower = []
    list3_upper = []
    for items in list3:

        if items < pivot:
            list3_lower.append(items)
        else:
            list3_upper.append(items)
    return quick_sorting_method2(list3_lower) + [pivot] + quick_sorting_method2(list3_upper)


if __name__ == '__main__':
    list1 = [56, 41, 12, 6, 31, 1, 19, 65, 22, 2]
    print('Before sorting with method1', list1)
    quick_sort(list1, 0, len(list1) - 1)
    print('Sorting list with method1 :', list1)

    list4 = [23, 24, 67, 8, 5, 1, 20, 0, 32, 3]
    print('Before sorting with method2 ', list4)
    print('Sorting list with method2 :', quick_sorting_method2(list4))
