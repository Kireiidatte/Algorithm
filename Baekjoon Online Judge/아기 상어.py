from collections import deque
import queue

N = int(input())
mat = [[*map(int, input().split())] for _ in range(N)]
# 아기 상어의 크기
shark_size = 2
# 물고기를 잡아먹을 수 있는 시간
time = 0

x, y = 0, 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#상어위치
for i in range(N):
    for j in range(N):
        if mat[i][j] == 9:
            x = i
            y = j

def bfs(x, y, shark_size):
    distance = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    q = deque()
    q.append((x, y))
    visited[x][y] = True
    # 거리가 가까운 물고기 위치를 담을 리스트
    shortest_list = []

    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0<= nx < N and 0<= ny < N and not visited[nx][ny]:
                if mat[nx][ny] <= shark_size:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[cur_x][cur_y] + 1
                    if mat[nx][ny] < shark_size and mat[nx][ny] != 0:
                        shortest_list.append((nx,ny,distance[nx][ny]))

    return sorted(shortest_list, key=lambda x: (-x[2],-x[0],-x[1]))

# 상어 크기 증가를 위한 잡아먹은 물고기 수
cnt = 0

while True:
    shark = bfs(x, y, shark_size)
    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청
    if len(shark) == 0:
        break

    nx, ny, dist = shark.pop()
    time += dist
    mat[x][y], mat[nx][ny] = 0, 0
    # 상어좌표를 먹은 물고기 좌표로 옮김
    x, y = nx, ny
    cnt += 1

    if cnt == shark_size:
        shark_size += 1
        cnt = 0

print(time)