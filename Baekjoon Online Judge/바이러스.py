from collections import deque

v = int(input())
e = int(input())

matrix = [[0]*(v + 1) for i in range(v + 1)]

for i in range(e):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

visit_list = [False] * (v + 1)
cnt = 0

dq = deque([1])
visit_list[1] = True

while dq:
    V = dq.popleft()
    cnt += 1
    for i in range(1, v+1):
        if not visit_list[i] and matrix[V][i] == 1:
            dq.append(i)
            visit_list[i] = True

print(cnt - 1)