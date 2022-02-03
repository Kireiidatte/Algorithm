import sys
from collections import deque
sys.setrecursionlimit(100000)

N = int(input())
mat = [[] for _ in range(N)]
visited = [False] * N
isCycle = [False] * N
dist = [-1] * N

for _ in range(N):
    a, b = map(int, input().split())
    mat[a-1].append(b-1)
    mat[b-1].append(a-1)

# 순환선인지 아닌지 판단하는 함수
def dfs(start, cur, cnt):
    global cycle
    if cur == start and cnt >= 2:
        cycle = True
        return 
    
    visited[cur] = True
    for i in mat[cur]:
        if not visited[i]:
            dfs(start, i, cnt+1):
        elif i == start and cnt >= 2:
            dfs(start, i, cnt)

# 각 역마다 순환역과 얼마나 떨어져 있는지 계산하는 함수
def bfs():
    global dist
    q = deque()

    for i in range(N):
        if isCycle[i]:
            dist[i] = 0
            q.append(i)
    
    while q:
        cur = q.popleft()

        for i in mat[cur]:
            if dist[i] == -1:
                q.append(i)
                dist[i] = dist[cur] + 1

for i in range(N):
    visited = [False] * N
    cycle = False
    dfs(i, i, 0)

    if cycle:
        isCycle[i] = True
    
bfs()

for i in dist:
    print(i, end=' ')


