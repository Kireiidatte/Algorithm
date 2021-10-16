n = int(input())
a = [[0] * 3 for _ in range(n)]
d = [[0] * 3 for _ in range(n)]

for i in range(n):
     a[i][0], a[i][1], a[i][2] = map(int, input().split())

for i in range(n):    
    d[i][0] = min(d[i-1][1], d[i-1][2]) + a[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + a[i][1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + a[i][2]
             
print(min(d[n - 1]))