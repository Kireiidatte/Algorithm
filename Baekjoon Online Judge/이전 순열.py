def pre_permutaion(list):
    i = len(list)-1
    j = len(list)-1
    while i>0 and list[i-1] <= list[i]:
        i -= 1
    if i<= 0:
        return False
    while list[j] >= list[i-1]:
        j -= 1 
    
    list[i-1], list[j] = list[j], list[i-1]
    j = len(list)-1
    while i < j:
        list[i],list[j] = list[j],list[i]
        i += 1
        j -= 1
    return True
N = int(input())
arr = list(map(int,input().split()))

if pre_permutaion(arr):
    print(' '.join(map(str, arr)))
else:
    print(-1)