def binarySearch(arr, key):
    left = 0
    right = len(arr) - 1

    while(left <= right):
        mid = (left + right) // 2
        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            left = mid + 1
        else:
            right  = mid - 1
    return -1

arr = [-1,0,3,5,9,12]
print(binarySearch(arr,9))