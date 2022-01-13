# Prim
import sys

def solution(n, costs):
    graph = {}
    visited = [False] * n
    D = [sys.maxsize] * n
    previous = [None] * n

    D[0], previous[0] = 0, 0
    vertices = 1

    for i in range(n):
        graph[i] = []
    for cost in costs:
        graph[cost[0]].append((cost[1], cost[2]))
        graph[cost[1]].append((cost[0], cost[2]))

    while True:
        if vertices == n:
            break

        min_vertex = -1 # min_vertex는 트리에 인접한 정점들 중 가중치가 가장 작은 간선으로 연결된 것
        min_value = sys.maxsize # min_value는 간선의 가중치임

        for v in range(n):
            if not visited[v] and D[v] < min_value:
                min_vertex = v
                min_value = D[v]
        
        visited[min_vertex] = True
        vertices += 1

        for adj_v, weight in graph[min_vertex]:
            if not visited[adj_v]:
                if weight < D[adj_v]:
                    D[adj_v] = weight
                    previous[adj_v] = min_vertex

    return sum(D[1:])

