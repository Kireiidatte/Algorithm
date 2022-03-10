N = int(input())
cnt = 0

def solve(n, start, to):
    global cnt
    if n == 0:
        return
    cnt += 1
    solve(n-1, start, 6-start-to)
    solve(n-1, 6-start-to, to)

def printSolve(n, start, to):
    if n == 0:
        return
    printSolve(n-1, start, 6-start-to)
    print('{0} {1}'.format(start, to))
    printSolve(n-1, 6-start-to, to)

solve(N, 1, 3)
print(cnt)
printSolve(N, 1, 3)

