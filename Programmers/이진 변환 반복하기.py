from collections import Counter

def solution(s):
    answer = []
    cnt = 0
    step = 0
    
    while s != '1':
        counter = Counter(s)
        removed_zero = 0
        step += 1
        cnt += counter['0']
        s = bin(len(s) - counter['0'])[2:]
    
    answer.append(step)
    answer.append(cnt)
    
    return answer