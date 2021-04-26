def JoyStick(name):
    answer = 0
    name = list(name)
    index = 0
    
    while(True):
        left = 1
        right = 1
        
        if name[index] != 'A':
            answer += min(ord(name[index]) - ord('A'), ord('Z') - ord(name[index]) + 1)
            
        name[index] = 'A'
        
        if name == ['A'] * len(name):    break
        
        for i in range(1, len(name)):
            if name[index + i] == 'A':    right += 1
            else: break
        
        for j in range(1, len(name)):
            if name[index - j] == 'A':    left += 1
            else: break
        
        if right > left:
            answer += left
            index -= left
        
        else:
            answer += right
            index += right
            
    return answer