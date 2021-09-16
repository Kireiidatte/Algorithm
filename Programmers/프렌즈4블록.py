def findSquare(board):
    m = len(board)
    n = len(board[0])
    tmp = []
    for j in range(n - 1):
        for i in range(m - 1): 
            if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] and board[i][j] != '_':
                tmp.append((i, j))
    
    return tmp

def fillBoard(board, tmp):
    for i, j in tmp:
        board[i][j] = 0
    for i, row in enumerate(board):
        print(i)
        empty = ['_'] * row.count(0)
        board[i] = empty + [block for block in row if block != 0]
        print(board[i])
        
    return board

def solution(m, n, board):
    block = 0
    board = [list(board[i]) for i in range(m)]
    
    while True:
        tmp = findSquare(board)
        if not tmp:    return block
        
        block += len(tmp) * 4
        for n in range(len(tmp) - 1):
            if tmp[n][0]+1 == tmp[n+1][0] and tmp[n][1]+1 == tmp[n+1][1]: 
                block -= 1
        board = fillBoard(board, tmp)
        
        
        
m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
board = list(map(list, zip(*board)))

print(board)

"""
2x2 정사각형 단위로 좌표를 탐색하면서 pop할 좌표를 찾는다.

그리고 pop할 블록을 찾으면, 따로 만들어둔 복제 배열에 해당 좌표를 0으로 마스킹한다.
- 이전에 pop된 블록은 -1, 지금 pop된 블록은 0으로 지정한다.

그리고 마지막에 0의 개수를 세고, pop된 자리에 위에 있던 블록을 떨궈주면 된다.


def solution(m, n, board):
    board = list(map(list, zip(*board)))
    
    def game(b):
        pops = 0
        sc = [i[:] for i in b]
        for i in range(1,n):
            for j in range(1,m):
                if b[i][j] == -1: continue
                if b[i][j] == b[i-1][j] == b[i-1][j-1] == b[i][j-1]:
                    sc[i][j], sc[i-1][j], sc[i-1][j-1], sc[i][j-1] = 0,0,0,0
        
        for i,v in enumerate(sc):
            cnt = v.count(0)
            pops += cnt
            sc[i] =[-1]*cnt + [a for a in v if a!=0]
        
        return sc, pops
    
    answer = 0
    while True:
        board, pops = game(board)
        if pops == 0:  return answer
        answer += pops
"""