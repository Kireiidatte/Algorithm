def isRight(st):
    stack = []
    
    for s in (st):
        if s == '(':
            stack.append(s)
        elif s == ')':
            if stack:
                stack.pop()
            else:
                return False
            
    return True

def devide(st):
    left = 0
    right = 0
    
    for i in range(len(st)):
        if st[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return st[:i+1], st[i+1:]

def solution(p):
    if not p:
        return ''

    u, v = devide(p)

    if isRight(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for s in u[1:len(u) - 1]:
            if s == '(':
                answer += ')'
            else:
                answer += '(' 

        return answer