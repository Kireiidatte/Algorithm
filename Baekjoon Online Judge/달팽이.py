N = int(input())
find_num = int(input())

mat = [[0] * N for _ in range(N)]

# 방향
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

mat[0][0] = N * N
x, y, = 0, 0
max_num = N * N - 1
direction = 0
t_x, t_y = 0, 0

while max_num > 0:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 0 <= nx < N and 0 <= ny < N and not mat[nx][ny]:
        mat[nx][ny] = max_num
        if max_num == find_num:
            t_x, t_y = nx, ny
        x, y = nx, ny
        max_num -= 1
    else:
        direction = (direction + 1) % 4

for row in mat:
    print(*row)
print(t_x + 1, t_y + 1)