def solution(s):
    lst = s.split(' ')
    for i in range(len(lst)):
        lst[i] = lst[i][:1].upper() + lst[i][1:].lower()
    
    return ' '.join(lst)