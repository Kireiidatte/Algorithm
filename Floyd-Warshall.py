# 모든 정점에서 모든 정점으로의 최단 경로 구할 때 쓰임(거쳐가는 정점을 기준으로 최단 거리 구함)
import sys

def floyd_warshall(adj_matrix):  # adj_matrix는 인접행렬임
                                 # adj[i][j]의 값은 정점 i와 j가 인접하면 간선의 가중치이고 아니면 sys.maxsize

    N = len(adj_matrix)

    # k = 거쳐가는 노드
    for k in range(N):
        # i = 출발 노드
        for i in range(N):
            # j = 도착 노드
            for j in range(N):
                adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][k] + adj_matrix[k][j])
    
    return adj_matrix