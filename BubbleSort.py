array = [8, 4, 6, 2, 9, 1, 3, 7, 5]

def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

print("before: ",array)
array = bubbleSort(array)
print("after:", array)


