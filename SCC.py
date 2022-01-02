# Finding Strongly Connected Component

def Korasaju(adj_matrix):  
    N, stack, BCClist = len(adj_matrix), [], []

    def dfs(v):
        visited[v] = True
        for adj_v in range(N):
            if adj_matrix[v][adj_v] and not visited[adj_v]:
                dfs(adj_v)
        stack.append(v)

    def reverse_dfs(v):
        visited[v] = True
        for adj_v in range(N):
            if adj_matrix[adj_v][v] and not visited[adj_v]:
                reverse_dfs(adj_v)
        bcclist.append(v)
    

    visited = False * [N]
    for v in range(N):
        if not visited[v]:
            dfs(v)

    visited = [False] * N
    while stack:
        v = stack.pop()
        if not visited[v]:
            bcclist = []
            reverse_dfs(v)
            BCClist.append(bcclist)
    
    return BCClist