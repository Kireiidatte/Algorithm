N = int(input())
nums = [*map(int, input().split())]

num_set = sorted(list(set(nums)))
num_dict = {}

for i in range(len(num_set)):
    num_dict[num_set[i]] = i

for num in nums:
    print(num_dict[num], end=' ')