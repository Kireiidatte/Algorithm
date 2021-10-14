N = int(input())
a = [0] + list(map(int, input().split()))
d= [10000000]*(N+1)
d[0] = 0

for i in range(1, N+1):
    for j in range(1,i+1):
        d[i] = min(d[i], d[i-j]+a[j])
print(d[N])
