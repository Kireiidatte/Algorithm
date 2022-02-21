def isPossible(queen, row):
    for i in range(row):
        if queen[i] == queen[row] or abs(queen[i] - queen[row]) == row - i:
            return False
    return True

def dfs(queen, row):
    n = len(queen)
    cnt = 0
    
    if n == row:
        return 1
    
    for col in range(n):
        queen[row] = col
        if isPossible(queen, row):
            cnt += dfs(queen, row + 1)
    
    return cnt

def solution(n):
    return dfs([0] * n, 0)