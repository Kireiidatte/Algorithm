def solution(n):
    count = 0
    
    for i in range(1, n // 2 + 1):
        tmp = 0
        for j in range(i, n + 1):
            if tmp > n:    break
            tmp += j
            if tmp == n:
                count += 1
                break
           
    
    return count + 1
