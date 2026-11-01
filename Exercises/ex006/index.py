def quick_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[0]

    less = []
    equal = []
    greater = []

    for element in arr:
        if element < pivot:
            less.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)

    return quick_sort(less) + equal + quick_sort(greater)
