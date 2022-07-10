N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins = coins[::-1]

cnt = 0

for coin in coins:
    q, d = divmod(K, coin)
    if q:
        cnt += q
        K -= q * coin
    if K == 0:
        break

print(cnt)
