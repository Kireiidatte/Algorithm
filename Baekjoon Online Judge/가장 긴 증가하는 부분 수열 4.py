n = int(input())
a = list(map(int,input().split()))
d = [0] * n
v = [-1] * n

for i in range(n):
    d[i] = 1
    for j in range(i):
        if a[j] < a[i] and d[j]+1 > d[i]:
            d[i] = d[j]+1
            v[i] = j

answer = max(d)
p = [idx for idx, x in enumerate(d) if x == answer][0]

print(answer)

def go(p):
    if p == -1:
        return
    go(v[p])
    print(a[p], end=' ')

go(p)