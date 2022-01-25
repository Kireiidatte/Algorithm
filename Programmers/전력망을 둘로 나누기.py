from collections import deque

def bfs(n, graph):
    cnt = 0
    visited = [False] * (n+1)
    visited[1] = True
    dq = deque([1])
    
    while dq:
        v = dq.popleft()
        cnt += 1
        for w in graph[v]:
            if not visited[w]:
                dq.append(w)
                visited[w] = True
    
    return cnt


def solution(n, wires):
    answer = []
    graph = {}

    for i in range(1, n+1):
        graph[i] = []
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    
    for wire in wires:
        graph[wire[0]].remove(wire[1])
        graph[wire[1]].remove(wire[0])
        answer.append(abs(n - 2*bfs(n, graph)))
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    
    return answer