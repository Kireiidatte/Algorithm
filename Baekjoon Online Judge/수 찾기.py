N = int(input())
nums = [*map(int, input().split())]
nums.sort()

M = int(input())
find = [*map(int, input().split())]

for n in find:
    left, right = 0, N-1
    flag = False

    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] > n:
            right = mid - 1
        elif nums[mid] < n:
            left = mid + 1
        else:
            flag = True
            print(1)
            break
    
    if not flag:
        print(0)