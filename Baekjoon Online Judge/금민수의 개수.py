from itertools import product

A, B = map(int, input().split())

cnt = 0

for i in range(len(str(A)), len(str(B))+1):
    lst = product([4, 7], repeat=i)
    for num in lst:
        n = int(''.join(map(str, num)))
        if A <= n <= B:
            cnt += 1

print(cnt)
