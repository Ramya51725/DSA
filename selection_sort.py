def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range (i+1 , n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i] , arr[min_idx] = arr[min_idx] , arr[i]
    return arr 

print (selection_sort([9,8,7,6,5,4,3,2,1]))


# Time complexity: O(n²)


# Selection sort is a simple way to sort numbers. It looks at 
# the whole list and finds the smallest number. Then it puts that 
# number in the first place. Next, it looks at the rest of the list, 
# finds the next smallest number, and puts it in the second place. It 
# keeps doing this again and again. Each time, it puts the correct smallest 
# number in the next position. In the end, all numbers are in the right order.


# function explanation


# This function sorts a list of numbers using selection sort. It first 
# finds the length of the list. Then it goes through each position one by 
# one. For every position i, it assumes that element is the smallest 
# (min_idx = i). Next, it checks the rest of the list (from i+1 to end) 
# to find the real smallest number. If it finds a smaller number, it updates 
# min_idx. After checking all elements, it swaps the smallest number with the 
# current position i. This way, the smallest number moves to the correct place. 
# It repeats this process for all positions until the list is sorted, and then 
# returns the sorted list.