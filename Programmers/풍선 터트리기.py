def solution(a):
    answer = 2
    leftMin = a[0]
    rightMin = a[-1]
    
    if len(a) <= 2:
        return len(a)
    
    for i in range(1, len(a) - 1):
        if leftMin > a[i]:
            answer += 1
            leftMin = a[i]
        if rightMin > a[-1-i]:
            answer += 1
            rightMin = a[-1-i]
 
    return answer if leftMin != rightMin else answer - 1