from itertools import permutations
from collections import deque

def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    elif op == '-':
        return str(int(num1) - int(num2))
    elif op == '*':
        return str(int(num1) * int(num2))

def calc(expression, op):
    dq = deque()
    tmp = ''

    # ['100', '-', '200', '*', '300', '-', '500', '+', '20']
    for e in expression:
        if e.isdigit():
            tmp += e
        else:
            dq.append(tmp)
            dq.append(e)
            tmp = ''
    dq.append(tmp)

    for o in op:
        stack = deque()
        while dq:
            tmp = dq.popleft()
            if tmp == o:
                stack.append(operation(stack.pop(), dq.popleft(), o))
            else:
                stack.append(tmp)
        dq = stack

    return abs(int(dq[0]))
        
def solution(expression):
    result = []
    ops = ['+', '-', '*']
    ops = list(permutations(ops, 3))

    for op in ops:
        result.append(calc(expression, op))
    
    return max(result)


