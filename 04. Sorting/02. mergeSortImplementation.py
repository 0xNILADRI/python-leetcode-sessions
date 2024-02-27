def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    m = len(arr)//2

    left = arr[:m]
    right = arr[m:]

    left = mergeSort(left)
    right = mergeSort(right)

    return  merge(left, right)

def  merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if (left[left_idx] < right[right_idx]):
            result.append(left[left_idx])
            left_idx += 1

        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result

arr = [64, 34, 25, 12, 22]
print(mergeSort(arr))