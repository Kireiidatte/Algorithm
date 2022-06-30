def solution(n):
    answer = [0] * (n + 1)
    answer[0] = 1
    sub = 0
    
    for i in range(2, n+1, 2):
        answer[i] = (answer[i - 2] * 3 + sub * 2) % 1000000007
        sub += answer[i - 2]
        
    return answer[n]