N = int(input())
mat = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            mat[i][j] = 1
    
cnt = 0
for row in mat:
    cnt += row.count(1)
print(cnt)