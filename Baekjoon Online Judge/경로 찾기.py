N = int(input())
graph = [[*map(int, input().split())] for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1

for g in graph:
    print(*g)