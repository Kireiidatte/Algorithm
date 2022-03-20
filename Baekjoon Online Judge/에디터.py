import sys

str1 = list(sys.stdin.readline().strip())
str2 = []

m = int(sys.stdin.readline())

for _ in range(m):
    cmd = list(sys.stdin.readline().split())
    
    if cmd[0] == 'L':
        if str1:
            str2.append(str1.pop())
    elif cmd[0] == 'D':
        if str2:
            str1.append(str2.pop())
    elif cmd[0] == 'B':
        if str1:
            str1.pop()
    else:
        str1.append(cmd[1])

str1.extend(reversed(str2))
print(''.join(str1))