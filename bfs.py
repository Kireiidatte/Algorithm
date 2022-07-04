from collections import deque

N, M, V = map(int, input().split())
matrix = [[0]*(N + 1) for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
visit_list = [False]*(N + 1)

def BFS(V):
    dq = deque([V])
    visit_list[V] = True
    while dq:
        V = dq.popleft()
        for i in range(1, N + 1):
            if not visit_list[i] and matrix[V][i] == 1:
                dq.append(i)
                visit_list[i] = True