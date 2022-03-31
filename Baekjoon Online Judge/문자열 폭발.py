S = list(input().rstrip())
T = list(input().rstrip())

stack = []

for i in range(len(S)):
    stack.append(S[i])
    if len(stack) >= len(T) and stack[-1] == T[-1]:
        if stack[-len(T):] == T:
            stack[-len(T):] = []

if stack:
    print(''.join(stack))
else:
    print('FRULA')
