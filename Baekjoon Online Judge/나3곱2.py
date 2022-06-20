N = int(input())
nums = [*map(int, input().split())]

result = []
first_val = nums[0]
max_power = 0

for i in range(N):
    tmp = nums[i]
    power = 0

    while tmp % 3 == 0:
        tmp //= 3
        power += 1
    if (power > max_power) or (power == max_power and nums[i] < first_val):
        max_power = power
        first_val = nums[i]

result.append(first_val)

for i in range(N):
    if result[-1] * 2 in nums:
        result.append(result[-1] * 2)
        continue
    if result[-1] % 3 == 0 and result[-1] // 3 in nums:
        result.append(result[-1] // 3)
        continue
    break

print(*result)