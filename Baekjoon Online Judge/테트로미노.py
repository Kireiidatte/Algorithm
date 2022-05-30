N, M = map(int, input().split())
mat = [[*map(int, input().split())] for _ in range(N)]
visited = [[False]*M for _ in range(N)]
# 모든 좌표 중 최댓값
max_val = max(map(max, mat))
ans = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, step, total):
    global ans
    # 탐색을 계속 진행해도 최댓값에 못 미치는 경우
    if ans >= total + max_val * (4 - step):
        return
    # 블록의 개수가 4개일 때 
    if step == 4:
        ans = max(ans, total)
        return 
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 새로운 좌표가 유효한 범위 내 있고 탐색이력이 없는 경우
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                # 2번째 블록 연결 후 'ㅏ','ㅓ','ㅗ','ㅜ' 만들기
                if step == 2:
                    visited[nx][ny] = True # 탐색기록
                    # 새로운 좌표에서 탐색하지 않고 기존 좌표로 돌아와 탐색재개
                    dfs(x, y, step+1, total+mat[nx][ny])
                    visited[nx][ny] = False # 탐색기록 제거

                visited[nx][ny] = True
                dfs(nx, ny, step+1, total+mat[nx][ny])
                visited[nx][ny] = False

for x in range(N):
    for y in range(M):
        visited[x][y] = True # 탐색기록
        dfs(x, y, 1, mat[x][y])
        visited[x][y] = False # 탐색기록 제거

print(ans)