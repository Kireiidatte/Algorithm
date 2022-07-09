from itertools import combinations

N, M = map(int, input().split())
cards = [*map(int, input().split())]

index = [*combinations(range(N), 3)]
sum_card = 0

for i in index:
    tmp_sum = cards[i[0]] + cards[i[1]] + cards[i[2]]
    if tmp_sum <= M:
        sum_card = max(tmp_sum, sum_card)

print(sum_card)