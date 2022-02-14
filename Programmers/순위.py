from collections import defaultdict

def dfs(graph, InOut, visited, i, base):
    visited[i] = True
    if i != base:
        # 출력하는 노드의 link 개수 증가
        InOut[base][1] += 1
        # 입력받는 노드의 link 개수 증가
        InOut[i][0] += 1
    for v in graph[i]:
        if not visited[v]:
            dfs(graph, InOut, visited, v, base)

def solution(n, results):
    answer = 0
    graph = [[] for _ in range(n)]
    # in, out 값을 [0, 0]으로 초기화
    InOut = defaultdict(lambda: [0, 0])
    
    for a, b in results:
        graph[a-1].append(b-1)
    
    for i in range(n):
        visited = [False] * n
        dfs(graph, InOut, visited, i, i)
    
    for i in range(n):
        if InOut[i][0] + InOut[i][1] == n - 1:
            answer += 1
        
    return answer