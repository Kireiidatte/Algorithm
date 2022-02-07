array = [8, 4, 6, 2, 9, 1, 3, 7, 5]

def mergeSort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])

    i, j, k = 0, 0, 0

    while i < len(left) and j <len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    
    return array
        
print("before: ",array)
array = mergeSort(array)
print("after:", array)
