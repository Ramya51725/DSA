def merge(a, b):
    c = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while i < len(a):
        c.append(a[i])
        i += 1

    while j < len(b):
        c.append(b[j])
        j += 1

    return c


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    a = arr[0:mid]
    b = arr[mid:]

    sorted_a = mergeSort(a)
    sorted_b = mergeSort(b)

    return merge(sorted_a, sorted_b)

print(mergeSort([5, 2, 8, 1, 3]))