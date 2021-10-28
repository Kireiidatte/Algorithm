from collections import deque

def bfs(v, visited, computers):
    dq = deque([v])
    visited[v] = True
    
    while dq:
        v = dq.popleft()
        for idx, i in enumerate(computers[v]):
            if v == idx:    continue
            if i == 1 and not visited[idx]:
                dq.append(idx)
                visited[idx] = True

def solution(n, computers):
    network = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, computers)
            network += 1
    
    return network
