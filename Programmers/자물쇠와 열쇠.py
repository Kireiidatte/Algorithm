def attach(x, y, m, key, board):
    for i in range(m):
        for j in range(m):
            board[x+i][y+j] += key[i][j]

def detach(x, y, m, key, board):
    for i in range(m):
        for j in range(m):
            board[x+i][y+j] -= key[i][j]

def rotate(key):
    m = len(key)
    result = [[0] * m for _ in range(m)]
    
    for i in range(m):
        for j in range(m):
            result[j][m-i-1] = key[i][j]
    
    return result

def check(board, m, n):
    for i in range(n):
        for j in range(n):
            if board[m+i][m+j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    board = [[0] * (m*2 + n) for _ in range(m*2 + n)]
    
    # 자물쇠를 중앙에 배치
    for i in range(n):
        for j in range(n):
            board[m+i][m+j] = lock[i][j]
    
    rotated_key = key
    # 회전을 90도 간격으로 진행
    for _ in range(4):
        rotated_key = rotate(rotated_key)
        # 키를 이동시키면서 lock과 비교
        for x in range(1, m+n):
            for y in range(1, m+n):
                # 열쇠 넣어보기
                attach(x, y, m, rotated_key, board)
                if check(board, m, n):
                    return True
                detach(x, y, m, rotated_key, board)
                
    return False