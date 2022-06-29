N = int(input())
mat = []

for _ in range(N):
    r, c = map(int, input().split())
    mat.append((r, c))

# 곱셈의 최소 횟수 행렬
dp = [[0]*N for _ in range(N)]

for i in range(1, N):
    for j in range(N - i):
        if i == 1:
            dp[j][j+1] = mat[j][0] * mat[j][1] * mat[j+i][1]
            continue
        
        dp[j][j+i] = 2 ** 32
        for k in range(j, j+i): 
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + mat[j][0] * mat[k][1] * mat[j+i][1])                
    
#맨 오른쪽 위 출력
print(dp[0][N-1])