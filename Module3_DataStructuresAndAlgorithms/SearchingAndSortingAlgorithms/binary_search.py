def binary_search(list1, search_element):
    low_ind = 0
    high_ind = len(list1) - 1
    found = False
    mid_ind = 0
    while low_ind <= high_ind and not found:
        mid_ind = (low_ind + high_ind) // 2
        if search_element == list1[mid_ind]:
            found = True
        elif search_element > list1[mid_ind]:
            low_ind = mid_ind + 1
        else:
            high_ind = mid_ind - 1
    if found:
        print(f'Searching Element found at index: {mid_ind}')
    else:
        print('Search element not found')


if __name__ == '__main__':
    list2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    # list3 = [1, 7, 5, 9, 3, 3, 13, 15, 17, 19]
    search = 11
    binary_search(list2, search)
