n = int(input())
mat = []
visited = [[False] * n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
ans = []

def dfs(i, j, cnt):
    visited[i][j] = True
    global nums
    if mat[i][j] == 1:
        nums += 1
        
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and mat[nx][ny] == 1:
                dfs(nx, ny, cnt)

for i in range(n):
    mat.append(list(map(int, input())))

nums = 0
for i in range(n):
    for j in range(n):
        if mat[i][j] == 1 and not visited[i][j]:
            dfs(i, j, cnt)
            ans.append(nums)
            nums = 0
            
print(len(ans))
ans.sort()
for i in ans:
    print(i)
            
    
