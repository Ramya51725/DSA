def bubbleSort(arr):
    n = len(arr)
    for i in range (n):
        swapped = False 
        for j in range (0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                swapped = True 
        if swapped == False :
             break 
    return arr
print(bubbleSort([9,8,7,6,5,4])) 


# Time complexity: O(n²)


# Bubble sort is a simple method to arrange numbers in order. 
# It looks at two numbers that are next to each other and checks 
# if they are in the correct order. If the first number is bigger, 
# it swaps them. It goes through the whole list like this many times. 
# After each round, the biggest number moves to the end of the list. 
# It keeps repeating this process until all the numbers are in the right order.



# the function explanation


# This function sorts a list of numbers using bubble sort.
# It checks the list many times. In each round, it looks at two 
# numbers next to each other. If the first number is bigger, it 
# swaps them. The variable swapped is used to check if any swap happens. 
# If no swap happens in a round, it means the list is already sorted, so 
# the loop stops early. After each round, the biggest number moves to the end. 
# Finally, the function returns the sorted list.