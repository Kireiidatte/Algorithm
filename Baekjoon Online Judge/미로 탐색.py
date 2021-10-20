from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
cnt = 0
visited = [[0]*m for _ in range(n)]
mat = []
dist_mat = []

for _ in range(n):
    mat.append(list(map(int, input()))) 

queue = deque([(0, 0)])
visited[0][0] = 1

while queue:
    x, y = queue.popleft()
    if x == n - 1 and y == m - 1:
        print(visited[x][y])
        break
    
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and mat[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))