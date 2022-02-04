import sys
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]

def dfs(i, j, visited, mat, w, h):
    visited[j][i] = True
    
    for k in range(8):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < w and 0 <= ny < h:
            if not visited[ny][nx] and mat[ny][nx] == 1:
                dfs(nx, ny, visited, mat, w, h)
                
while(True):
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    mat = []
    visited = [[False]*w for _ in range(h)]
    for _ in range(h):
        mat.append(list(map(int, input().split())))
    
    cnt = 0
    
    for i in range(h):
        for j in range(w):
            if mat[i][j] == 1 and not visited[i][j]:
                dfs(j, i, visited, mat, w, h)
                cnt += 1
                
    print(cnt)