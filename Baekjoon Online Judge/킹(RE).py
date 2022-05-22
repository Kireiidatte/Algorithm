dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]
move = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

king, stone, N = input().split()

k_loc = [alpha.index(king[0]), int(king[1])]
s_loc = [alpha.index(stone[0]), int(stone[1])]

for _ in range(int(N)):
    idx = move.index(input())

    nx = k_loc[0] + dx[idx]
    ny = k_loc[1] + dy[idx]

    if nx < 0 or ny < 1 or nx > 7 or ny > 8:
        continue
    # 킹 위치와 돌 위치가 같은 경우
    if nx == s_loc[0] and ny == s_loc[1]:
        px = s_loc[0] + dx[idx]
        py = s_loc[1] + dy[idx]

        if px < 0 or py < 1 or px > 7 or py > 8:
            continue
    
        s_loc[0] = px
        s_loc[1] = py
    
    k_loc[0] = nx
    k_loc[1] = ny

k_final_loc = alpha[k_loc[0]] + str(k_loc[1])
s_final_loc = alpha[s_loc[0]] + str(s_loc[1])
print(k_final_loc)
print(s_final_loc)