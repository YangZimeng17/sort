def merge_sort(L):
    # both empty or list of 1 element return a copy of itself
    if len(L) <= 1:
        return L[:]

    # seperate L into 2 halves, then sorted
    mid = len(L) // 2
    first_half = merge_sort(L[:mid])
    second_half = merge_sort(L[mid:])

    # merge 2 sorted half
    list = []
    p1 = 0
    p2 = 0

    # use 2 pointer to compare elements in 2 half lists and add elements into new list in non-decreasing sequence
    while True:
        if first_half[p1] < second_half[p2]:
            list.append(first_half[p1])
            p1 += 1
        else:
            list.append(second_half[p2])
            p2 += 1

        if p1 > len(first_half) - 1 or p2 > len(second_half) - 1:
            break

    # add left over elements of 2 half lists to new list
    list += first_half[p1:]
    list += second_half[p2:]

    return list

L = [3,1,5,2,4,8,6,7,9]
print(merge_sort(L))
L1 = [2,1]
print(merge_sort(L1))
L2 = [3]
print(merge_sort(L2))
L3 = []
print(merge_sort(L3))