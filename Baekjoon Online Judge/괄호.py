import sys

num = int(sys.stdin.readline())

def isValid(ps):
    cnt = 0

    for p in ps:
        if p == '(':
            cnt += 1
        else:
            cnt -=1
        if cnt < 0:
            return 'NO'
    
    if cnt == 0:
        return 'YES'
    else:
        return 'NO'
    
for i in range(num):
    print(isValid(sys.stdin.readline().strip()))
