import enum


nums = list(map(int, input().split()))
target = int(input())

def twoSum(nums, target):
    nums_map = {}

    for idx, num in enumerate(nums):
        nums_map[num] = idx
    
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return nums.index(num), nums_map[target - num]
