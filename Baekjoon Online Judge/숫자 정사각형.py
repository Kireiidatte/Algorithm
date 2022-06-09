N, M = map(int, input().split())

mat = [list(input()) for _ in range(N)]
max_square = 1
max_range = min(N, M)

for i in range(N):
    for j in range(M):
        for k in range(max_range):
            if i+k < N and j+k < M and len(set([mat[i][j], mat[i+k][j], mat[i][j+k], mat[i+k][j+k]])) == 1:
                max_square = max(max_square, (k+1)**2)
                
print(max_square)