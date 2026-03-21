def binarySearch(arr, x):
    low = 0
    high = len (arr) - 1 
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid 
        elif arr[mid] < x:
            low = mid +1 
        else:
            high = mid - 1 
    return ("Element not found")

print(binarySearch([1,2,3,4,4,5,5], 9))

# Time complexity: O(log n)
# O(log n) means:
# “Keep dividing the list into half until you find the answer”
# What is O(log n)?
# O(log n) means the problem size becomes half again and again.


# Binary search is a fast way to find a number in a sorted list. 
# It starts by checking the middle element of the list. If the middle 
# number is the one we want, the search is done. If the target number is 
# smaller, it searches only in the left half. If the target number is bigger, 
# it searches only in the right half. It keeps dividing the list into halves 
# and checking the middle each time. This process continues until the number 
# is found or the list becomes empty.

