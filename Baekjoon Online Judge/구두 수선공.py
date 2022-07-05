N = int(input())
pair = []

for i in range(1, N+1):
    a, b = map(int, input().split())
    pair.append([i, a/b])

pair.sort(key=lambda x: (x[1], x[0]))

for p in pair:
    print(p[0], end=' ')