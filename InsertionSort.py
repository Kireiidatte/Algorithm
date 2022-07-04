array = [8, 4, 6, 2, 9, 1, 3, 7, 5]

def insertionSort(array):
    # 첫 번째 값은 정렬이 됐다고 가정
    for i in range(1, len(array)):
        # 뒤에서 하나씩 비교
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]

print("before: ",array)
array = insertionSort(array)
print("after:", array)
