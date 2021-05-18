from collections import deque

def solution(numbers, target):
    answer = 0
    dq = deque([(0, 0)]) 
    
    while dq:
        s, l = dq.popleft()
        
        if l > len(numbers):    break
        elif l == len(numbers) and s == target:
            answer += 1
        
        dq.append((s + numbers[l - 1], l + 1))
        dq.append((s - numbers[l - 1], l + 1))

    return answer
