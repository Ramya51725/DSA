def search(arr , x):
    for i in range (len(arr)):
        if arr[i] == x:
            return i
    return "Element Not Found"

print(search([1,2,3,5,6,8] , 1))

# Time complexity: O(n)

# Linear search is a simple way to find a number in a list. It 
# checks each element one by one, starting from the first element. 
# It compares each element with the number we are looking for. If it 
# finds the number, it stops and returns the position. If it reaches 
# the end of the list and does not find the number, it means the number 
# is not in the list

