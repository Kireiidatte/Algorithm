from itertools import combinations
# 문제수, L <= 문제 난이도의 합 <= R, 가장 어려운 문제 난이도 - 가장 쉬운 문제 난이도 >= X
N, L, R, X = map(int, input().split())

problem = [*map(int, input().split())]
result = 0

for i in range(2, N+1):
    for comb in combinations(problem, i):
        if L <= sum(comb) <= R:
            if max(comb) - min(comb) >= X:
                result += 1

print(result)