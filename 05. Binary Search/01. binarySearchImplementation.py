def binarySearch(arr, key):
    left = 0
    right = len(arr) - 1

    while(left <= right):
        mid = (left + right) // 2
        if key < mid:
            right  = mid - 1
        elif key > mid:
            left = mid + 1
        else:
            return mid
    return -1

arr = [1,2,3,4,5,6,7,8]
print(binarySearch(arr,2))