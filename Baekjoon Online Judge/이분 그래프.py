# 탐색하면서 서로 다른 색깔로 coloring하는게 포인트
import sys
sys.setrecursionlimit(1000000)

n = int(input())

for _ in range(n):
    v, e = map(int, sys.stdin.readline().split())
    mat = [[] for _ in range(v)]
    color = [0] * v
    
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        mat[a-1].append(b-1)
        mat[b-1].append(a-1)

    def dfs(x, c):
        color[x] = c

        for y in mat[x]:
            if color[y] == 0:
                if not dfs(y, 3-c):
                    return False
            elif color[y] == color[x]:
                return False
        return True

    bipartite = True

    for i in range(v):
        if color[i] == 0:
            if not dfs(i, 1):
                bipartite = False

    print('YES' if bipartite else 'NO')
