from collections import deque

def solution(priorities, location):
    answer = 0
    dq = deque(priorities)

    while True:
        max_elem = max(dq)
        tmp = dq.popleft()
        
        if max_elem == tmp:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
        else:
            dq.append(tmp)
            if location == 0:
                location = len(dq) - 1
            else:
                location -= 1
    
    return answer