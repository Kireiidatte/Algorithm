from collections import deque

# 보드의 크기
N = int(input())
# 사과의 위치
K = int(input())
# 뱀의 위치
snake = deque([[0, 0]])

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

mat = [[0]*N for _ in range(N)]

for _ in range(K):
    x, y = map(int, input().split())
    mat[x-1][y-1] = 1

# 뱀의 방향 변환 정보
L = int(input())

cmd = {}
for _ in range(L):
    X, C = input().split()
    cmd[int(X)] = C

time = 0
direction = 1
x, y = 0, 0

def change_direction(direction, c):
    if c == 'D':
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    
    return direction

while True:
    time += 1
    x += dx[direction]
    y += dy[direction]

    if time in cmd.keys():
        direction = change_direction(direction, cmd[time])
    
    # 벽에 부딪히지 않으면 
    if 0 <= x < N and 0 <= y < N:
        # 몸에 부딪힌 경우
        if [x, y] in snake:
            break
        # 다음 위치에 사과가 있는 경우
        if mat[x][y] == 1:
            mat[x][y] = 0
            snake.append([x, y])
        # 다음 위치에 사과가 없는 경우
        elif mat[x][y] == 0:
            snake.append([x, y])
            snake.popleft()
    # 벽에 부딪혔을 때 
    else:
        break

print(time)