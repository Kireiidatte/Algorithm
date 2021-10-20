import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    mat[b].append(a)
    mat[a].append(b)

visited = [False] * (n+1)
cc_cnt = 0

def bfs(v):
    dq = deque([v])
    visited[v] = True
    while dq:
        v = dq.popleft()
        for i in mat[v]:
            if not visited[i]:
                dq.append(i)
                visited[i] = 1
    
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cc_cnt += 1

print(cc_cnt)

