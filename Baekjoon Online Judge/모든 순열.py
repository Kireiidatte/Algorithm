from itertools import permutations

N = int(input())

lst = [*permutations([i for i in range(1, N+1)])]

for l in lst:
    print(*l)
