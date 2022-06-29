M, N = map(int, input().split())

mat = [[0] * N for _ in range(M)]

# 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y, = 0, 0
mat[0][0] = M * N
max_num = M * N - 1
direction = 0
change_direction = 0

while max_num > 0:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 0 <= nx < M and 0 <= ny < N and not mat[nx][ny]:
        mat[nx][ny] = max_num
        x, y = nx, ny
        max_num -= 1
    else:
        change_direction += 1
        direction = (direction + 1) % 4

print(change_direction)