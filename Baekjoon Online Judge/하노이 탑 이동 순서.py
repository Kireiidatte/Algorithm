N = int(input())

def solve(n, start, to):
    if n == 0:
        return
    solve(n-1, start, 6-start-to)
    print('{0} {1}'.format(start, to))
    solve(n-1, 6-start-to, to)
    
print((1 << N) - 1)
solve(N, 1, 3)

