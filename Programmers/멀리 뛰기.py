def solution(n):
    answer = []
    answer.append(1)
    answer.append(2)
    
    for i in range(2, n):
        answer.append(answer[i - 1] + answer[i - 2])
        answer[i] %= 1234567
        
    return answer[n - 1]