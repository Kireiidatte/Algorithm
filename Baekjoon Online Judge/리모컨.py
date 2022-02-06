n = int(input())
m = int(input())

a = []
if m > 0:
    a = list(map(int, input().split()))

broken = [False] * 10
for i in a:
    broken[i] = True

def isPossible(c):
    if c == 0:
        return 0 if broken[0] else 1
    
    l = 0

    while c > 0:
        if broken[c % 10]:
            return 0
        l += 1
        c //= 10
    
    return l

ans = abs(n-100)

for i in range(1000001):
    c = i
    l = isPossible(c)
    if l > 0:
        press = abs(c-n)
        if ans > l + press:
            ans = l + press

print(ans)