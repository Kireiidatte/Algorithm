def solution(n, money):
    answer = [1] + [0 for i in range(n)]
    
    for i in money:
        for j in range(i, n + 1):
            if j >= i:
                answer[j] += answer[j - i]
              
    return answer[n] % 1000000007