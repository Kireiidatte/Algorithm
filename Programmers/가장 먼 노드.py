from collections import deque

def solution(n, edge):
    answer = 0
    graph = {}
    visited = [0] * n
    
    for i in edge:
        graph[i[0]] = graph.get(i[0], []) + [i[1]]
        graph[i[1]] = graph.get(i[1], []) + [i[0]]
    
    queue = deque([1])
    visited[0] = 1
    
    while queue:
        nodes = len(queue)
        for i in range(nodes):
            n = queue.popleft()
            for j in graph[n]:
                if visited[j - 1] == 0:
                    visited[j - 1] = 1
                    queue.append(j)
    
    return nodes