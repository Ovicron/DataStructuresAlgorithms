# Find First Entry in List with Duplicates
# Find Last Entry in a List with Duplicates

def first_occurrence(lst, k):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if lst[mid] < k:
            low = mid + 1
        elif lst[mid] > k:
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            if lst[mid - 1] != k:
                return mid
            high = mid - 1
    return -1


def last_occurrence(lst, k):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if lst[mid] < k:
            low = mid + 1
        elif lst[mid] > k:
            high = mid - 1
        else:
            if mid + 1 == len(lst):
                return mid
            if lst[mid + 1] != k:
                return mid
            low = mid + 1
    return -1


x = [11, 15, 23, 25, 34, 51, 51, 51, 74]
print(first_occurrence(x, 51))
print(last_occurrence(x, 51))
