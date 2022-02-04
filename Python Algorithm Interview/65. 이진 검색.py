from bisect import bisect_left

def search(nums, target):
    idx = bisect_left(nums, target)
    if idx < len(nums) and nums[idx] == target:
        return idx
    else:
        return -1