def getDivisors(num):
    # 1일 때 약수의 개수는 1
    if num == 1:
        return 1
    
    cnt = 0
    
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            cnt += 1
    
    return cnt + 2
    
def solution(left, right):
    answer = 0
    
    while left <= right:
        tmp = getDivisors(left)
        if tmp % 2:
            answer -= left
        else:
            answer += left
        left += 1
        
    return answer