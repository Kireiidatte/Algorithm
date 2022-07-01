import sys

N = int(input())
mat = [[*map(int, input().split())] for _ in range(N)]

minimum = sys.maxsize
selected = [False for _ in range(N)]

def dfs(idx, cnt):
    global minimum
    if cnt == N / 2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if selected[i] and selected[j]:
                    start += mat[i][j]
                elif not selected[i] and not selected[j]:
                    link += mat[i][j]
        
        minimum = min(minimum, abs(start - link))
    
    for i in range(idx, N):
        if not selected[i]:
            selected[i] = True
            dfs(i+1, cnt+1)
            selected[i] = False
            
dfs(0, 0)

print(minimum)