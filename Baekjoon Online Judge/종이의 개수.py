N = int(input())

mat = []
for _ in range(N):
    mat.append([*map(int, input().split())])

cnt = {-1:0, 0:0, 1:0}

def isSame(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if mat[x][y] != mat[i][j]:
                return False
    
    return True

def solve(x, y, n):
    if isSame(x, y, n):
        cnt[mat[x][y]] += 1
    else:
        m = n // 3
        for i in range(3):
            for j in range(3):
                solve(x + i*m, y + j*m, m)

solve(0, 0, N)

print(cnt[-1])
print(cnt[0])
print(cnt[1])