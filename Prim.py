import sys

def Prim(graph, start, N): # graph[v]는 정점 v에 인접한 (정점, 가중치)의 리스트
                           # start는 트리에 처음으로 추가될 정점임
                           # N은 정점의 개수임
    
    visited = [False] * N  # visited[i]의 값은 정점 i가 트리에 속하면 True이고 아니면 False임    
    D = [sys.maxsize] * N 
    previous = [None] * N  # previous[i]의 값은 D[i]의 값을 갱신시킨 정점임 
    
    D[start], previous[start] = 0, start
    
    vertices = 1  # 트리에 추가된 정점의 수
    while True:
     
        if vertices == N:  # 트리에 존재하는 정점의 수가 N이 되면
            break  # 실행 중지하기
        
        min_vertex = -1  # min_vertex는 트리에 인접한 정점들 중 가중치가 가장 작은 간선으로 연결된 것임
        min_value = sys.maxsize  # min_value는 이 간선의 가중치임
        
        for v in range(N):
            if not visited[v] and D[v] < min_value:
                min_vertex = v
                min_value = D[v]
                
        visited[min_vertex] = True  # min_vertex를 트리에 추가하기
        vertices += 1
        
        for adj_v, weight in graph[min_vertex]:  # min_vertex에 인접한 정점들인 adj_v에 대해
            if not visited[adj_v]:  # adj_v가 트리에 속하지 않은 동시에
                if weight < D[adj_v]:  # min_vertex와 adj_v를 잇는 간선의 가중치가 D[adj_v]보다 작다면
                    D[adj_v] = weight  # D[adj_v] 갱신하기
                    previous[adj_v] = min_vertex  # D[adj_v]가 min_vertex에 의해 갱신되었음을 나타내기
    
    mst = [[v, previous[v]] for v in range(1, N)]  # mst는 트리에 추가된 간선들의 집합
    cost = sum(D[1:])  # cost는 트리에 추가된 간선들의 가중치 합
    
    return mst, cost