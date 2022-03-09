from collections import Counter

N = int(input())
sang_card = Counter([*map(int, input().split())])
M = int(input())
card_set = [*map(int, input().split())]

card_cnt = [0] * M

for i in range(M):
    if card_set[i] in sang_card.keys():
        card_cnt[i] += sang_card[card_set[i]]

for i in card_cnt:
    print(i, end=' ')