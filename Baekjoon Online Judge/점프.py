N = int(input())
mat = [[*map(int, input().split())] for _ in range(N)]

# 방문 횟수
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break

        d = i + mat[i][j]
        r = j + mat[i][j]

        if d < N:
            dp[d][j] += dp[i][j]
        if r < N:
            dp[i][r] += dp[i][j]

print(dp)
print(dp[N-1][N-1])