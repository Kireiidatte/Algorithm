# Depth First Search

N, M, V = map(int, input().split())
matrix = [[0]*(N + 1) for i in range(N + 1)]

visit_list = [False] * (N + 1)

def dfs(vertex):
    visit_list[vertex] = True;
    for i in range(1, N + 1):
        if not visit_list[i] and matrix[V][i]:
            dfs(i)