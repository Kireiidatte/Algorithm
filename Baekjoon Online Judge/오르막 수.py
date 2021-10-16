mod = 10007
n = int(input())

d = [[0] * 10 for _ in range(n)]

for i in range(10):
    d[0][i] = 1

for i in range(1, n):
    for j in range(10):
        for k in range(j+1):
            d[i][j] += d[i - 1][k]
            d[i][j] %= mod

print(sum(d[n - 1]) % mod)
    
