# Topological Sort
# 사이클이 없는 그래프에서만 적용 가능

def TS(adj_list):
    visited = [False] * len(adj_list)  # visited[i]의 값은 정점 i를 방문했다면 True 아니면 False
    TSlist = []  # 방문한 정점들이 담길 리스트

    def dfs(v): 
        visited[v] = True
        for adj_v in adj_list[v]:  # 정점 v에서 출발하여 도착할 수 있는 정점들 adj_v에 대해
            if not visited[adj_v]:  # adj_v를 아직 방문하지 않았다면
                dfs(adj_v)  # adj_v에서부터 다시 탐색 시작하기 

        TSlist.append(v)  # 정점 v에서 출발하여 도착할 수 있는 정점들을 전부 방문했다면 리스트에 정점 v 추가

    for v in range(len(adj_list)):
        if not visited[v]:
            dfs(v)
    
    return list(reversed(TSlist))