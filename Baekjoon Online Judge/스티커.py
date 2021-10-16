T = int(input())

for _ in range(T):
    n = int(input())
    d = [[0]*3 for _ in range(n+1)]
    t1 = [0] + list(map(int, input().split()))
    t2 = [0] + list(map(int, input().split()))
    a = list(zip(t1, t2))  
    
    for i in range(1, n +1 ):
        d[i][0] = max(d[i - 1])
        d[i][1] = max(d[i - 1][0],d[i - 1][2]) + a[i][0]
        d[i][2] = max(d[i - 1][0],d[i - 1][1]) + a[i][1]
    print(max(d[n]))    