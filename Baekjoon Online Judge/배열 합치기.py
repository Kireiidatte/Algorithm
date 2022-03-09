N, M = map(int, input().split())

arrayA = [*map(int, input().split())]
arrayB = [*map(int, input().split())]
sortedArray = []

i, j = 0, 0

while i < N and j < M:
    if arrayA[i] <= arrayB[j]:
        sortedArray.append(arrayA[i])
        i += 1
    else:
        sortedArray.append(arrayB[j])
        j += 1
    
while i < N:
    sortedArray.append(arrayA[i])
    i += 1
while j < M:
    sortedArray.append(arrayB[j])
    j += 1

for i in sortedArray:
    print(i, end=' ')