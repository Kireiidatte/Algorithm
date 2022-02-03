n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(str, input())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = False

def dfs(startX, startY, curX, curY, cnt, color):
    global ans
    if ans:
        return
    
    visited[curX][curY] = True

    if startX == curX and startY == curY and cnt >= 4:
        ans = True
        return 
    
    for k in range(4):
        nx = curX + dx[k]
        ny = curY + dy[k]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and color == mat[nx][ny]:
                dfs(startX, startY, nx, ny, cnt+1, color)
            elif nx == startX and ny == startY and cnt >= 4:
                dfs(startX, startY, nx, ny, cnt, color)
                    
    return    

for i in range(n):
    for j in range(m):
        visited = [[False] * m for _ in range(n)]
        visited[i][j] = True
        dfs(i, j, i, j, 1, mat[i][j])
        
print('Yes' if ans else 'No')

