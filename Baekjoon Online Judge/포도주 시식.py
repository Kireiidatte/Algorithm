n = int(input())
wine = [0]
d = [0] * (n+1)

for _ in range(n):
    wine.append(int(input()))

d[1] = wine[1]
if n >= 2:
    d[2] = wine[1] + wine[2] 

for i in range(3, n+1):
    d[i] = max(d[i-1], d[i-2]+wine[i], d[i-3]+wine[i-1] + wine[i])

print(d[n])

    






