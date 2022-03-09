N = int(input())
sang_card = [*map(int, input().split())]
M = int(input())
card_set = [*map(int, input().split())]

sang_card.sort()

def findNum(num):
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2
        if sang_card[mid] == num:
            return True
        elif sang_card[mid] > num:
            right = mid - 1
        else:
            left = mid + 1

    return False

hasCards = [0] * M
for i in range(M):
    if findNum(card_set[i]):
        hasCards[i] = 1

for i in hasCards:
    print(i, end=' ')
