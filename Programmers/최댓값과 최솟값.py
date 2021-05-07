def MaxMin(s):
    answer = ''
    s = list(map(int, list(s.split())))
    
    answer += str(min(s))
    answer += ' '
    answer += str(max(s))
    
    return answer