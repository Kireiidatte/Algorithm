from itertools import permutations

A, B = input().split()
B = int(B)
nums = [*permutations(A, len(A))]
answer = -1

for num in nums:
    if num[0] == '0':
        continue
    n = int(''.join(num))
    if n < B:
        answer = max(answer, n)

print(answer)