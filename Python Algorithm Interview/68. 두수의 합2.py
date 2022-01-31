def twoSum(numbers, target):
    for idx, val in enumerate(numbers):
        left, right = idx + 1, len(numbers) - 1
        expected = target - val

        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] < expected:
                left = mid + 1
            elif numbers[mid] > expected:
                right = mid - 1
            else:
                return idx+1, mid+1
