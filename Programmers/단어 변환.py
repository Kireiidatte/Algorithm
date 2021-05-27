from collections import deque

def solution(begin, target, words):
    
    def IsExchangeable(target, word):
        difference = 0
        
        for i in range(len(target)):
            if target[i] != word[i]:
                difference += 1
        
        if difference == 1:    return True
        else:    return False
    
    answer = 0
    dq = deque()
    dq.append((begin, 0))
    
    visited = [0] * len(words)
    
    if target not in words:
        return answer
    
    while dq:
        word = dq.popleft()
        
        if word[0] == target:
            return word[1]
        
        for i in range(len(words)):
            if IsExchangeable(word[0], words[i]) and visited[i] == 0:
                dq.append((words[i], word[1] + 1))
                visited[i] = 1
                
    return 0