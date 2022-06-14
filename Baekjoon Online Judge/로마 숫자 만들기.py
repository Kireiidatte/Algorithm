from itertools import combinations_with_replacement

N = int(input())
nums = [1, 5, 10, 50]
result = []

for i in combinations_with_replacement(range(4), N):
    hap = 0
    for j in i:
        hap += nums[j]
    result.append(hap)

print(len(set(result)))