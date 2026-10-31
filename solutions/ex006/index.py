def quick_sort(arr):
    # Base case: empty or single element list is already sorted
    if len(arr) <= 1:
        return arr.copy()

    # Choose pivot (using first element)
    pivot = arr[0]

    # Partition into three sublists
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

    # Recursively sort and concatenate
    return quick_sort(less) + equal + quick_sort(greater)
