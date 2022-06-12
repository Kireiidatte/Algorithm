from collections import deque

N, K = map(int, input().split())
lst = deque([i for i in range(1, N+1)])

print('<', end = '')

for i in range(N - 1):
    for _ in range(K - 1):
        lst.append(lst.popleft())
    print(f'{lst.popleft()}, ', end='')
print(f'{lst.pop()}>', end='')