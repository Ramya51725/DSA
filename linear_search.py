def search(arr , x):
    for i in range (len(arr)):
        if arr[i] == x:
            return i
    return "Element Not Found"

print(search([1,2,3,5,6,8] , 1))