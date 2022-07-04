from collections import deque, defaultdict

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

computer_list = []
max_cnt = 0

def BFS(V):
    visit_list = [False]*(N + 1)
    dq = deque([V])
    visit_list[V] = True
    cnt = 1

    while dq:
        V = dq.popleft()
        for v in graph[V]:
            if not visit_list[v]:
                dq.append(v)
                visit_list[v] = True
                cnt += 1

    return cnt

for i in range(1, N+1):
    cnt = BFS(i)
    if cnt > max_cnt:
        max_cnt = cnt
    computer_list.append([i, cnt])

for i, cnt in computer_list:
    if cnt == max_cnt:
        print(i, end = ' ')