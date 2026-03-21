def insertion_sort(arr):
    n= len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr 
print(insertion_sort([23, 1, 10, 5, 2]))


# Best case: O(n) (already sorted)

# Worst case: O(n²) (reverse order)


# Insertion Sort works by dividing the array into two parts: 
# a sorted part and an unsorted part. Initially, the first element
# is considered sorted, and the rest are unsorted. Then, one by one,
# elements from the unsorted part are picked and placed into their 
# correct position in the sorted part. To do this, the algorithm compares
# the current element with the elements before it and shifts all larger 
# elements one position to the right to create space. Once the correct spot 
# is found, the element is inserted there. This process repeats until all elements
# are placed in order, resulting in a fully sorted array.


# the function explanation


# Your function implements Insertion Sort, which works by building 
# a sorted portion of the array step by step. It starts from the second 
# element (i = 1) and treats the first element as already sorted. For each 
# element, it stores the current value in a variable called key, then compares 
# it with the elements before it (moving backwards using j). While the elements 
# in the sorted portion are larger than the key, they are shifted one position to 
# the right to make space. Once the correct position is found, the key is inserted 
# there (arr[j + 1] = key). This process repeats for every element, gradually expanding 
# the sorted portion until the entire array is sorted.