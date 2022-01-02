# Finding Connected Component

def cc(adj_list):
    visited = [False] * len(adj_list)  # vistied[i]의 값은 정점 i를 방문했다면 True, 아니면 False
    CCList = []  # 연결성분들이 담길 리스트

    def dfs(v):
        visited[v] = True
        ccList.append(v)

        for adj_v in adj_list[v]:  # 방금 방문한 정점 v에 인접한 정점들 adj_v에 대해서 
            if not visited[adj_v]:  # adj_v를 아직 방문하지 않았다면 
                dfs(adj_v)  # adj_v에서 다시 탐색 시작하기
        
    for v in range(len(adj_list)):
        if not visited[v]:
            ccList = []
            dfs(v)
            CCList.append(ccList)
    
    return CCList
