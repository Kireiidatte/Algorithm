from collections import deque

def solution(maps):
    x_move = [1, 0, -1, 0]
    y_move = [0, 1, 0, -1]
    
    m, n = len(maps), len(maps[0])
    dq = deque([(0, 0, 1)])
    
    while dq:
        x, y, cnt = dq.popleft()
        
        for i in range(4):
            nx = x + x_move[i]
            ny = y + y_move[i]
            
            if nx > -1 and ny > -1 and nx < n and ny < m:
                if maps[ny][nx] == 1 or maps[ny][nx] > cnt + 1:
                    maps[ny][nx] = cnt + 1
                    if nx == n - 1 and ny == m - 1:
                        return cnt + 1
                    
                    dq.append((nx, ny, cnt + 1))
    
    return -1 