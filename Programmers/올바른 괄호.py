def solution(s):
    stack = []
    s = list(s)
    
    for par in s:
        if par == '(':    
            stack.append(par)
        elif par == ')' and len(stack):    
            stack.pop()
        else:    
            return False
    
    if len(stack):    return False
    
    return True 
