from collections import deque

m, n = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]
dq = deque([])

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            dq.append([i, j])

def bfs():
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                dq.append([nx, ny])

bfs()

for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
    
print(res - 1)