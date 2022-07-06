n = int(input())
start, end = map(int, input().split())

relations = int(input())
adj_mat = [[] for _ in range(n + 1)]

for _ in range(relations):
    src, dest = map(int, input().split())
    adj_mat[src].append(dest)
    adj_mat[dest].append(src)

visited = [0] * (n+1)

def dfs(node):
    for n in adj_mat[node]:
        if not visited[n]:
            visited[n] += visited[node] + 1
            dfs(n)

dfs(start)
print(visited[end] if visited[end] > 0 else -1)