from collections import deque

MAX = 100000

n, k = map(int, input().split())
check = [False] * (MAX + 1)
dist = [0] * (MAX + 1)

check[n] = True
queue = deque([n])

while queue:
    now = queue.popleft()
    if now-1 >= 0:
        if not check[now-1]:
            queue.append(now-1)
            check[now-1] = True
            dist[now-1] = dist[now] + 1
    if now+1 <= MAX:
        if not check[now+1]:
            queue.append(now+1)
            check[now+1] = True
            dist[now+1] = dist[now] + 1     
    if now*2 <= MAX:
        if not check[now*2]:
            queue.append(now*2)
            check[now*2] = True
            dist[now*2] = dist[now] + 1     

print(dist[k])
