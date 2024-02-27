def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i - 1
        while( j>= 0 and arr[j] > arr[j+1]):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j -= 1
    return arr


array = [8,2,4,1,6,9]
print(insertionSort(array))