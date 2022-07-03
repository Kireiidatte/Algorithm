N = int(input())

consulting = [[*map(int, input().split())] for _ in range(N)]

# dp[i]는 i번째날까지 일을 했을 때 최대값
dp = [0] * (N + 1)

for i in range(N-1, -1, -1):
    if i + consulting[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(consulting[i][1] + dp[i + consulting[i][0]], dp[i+1])

print(dp[0])