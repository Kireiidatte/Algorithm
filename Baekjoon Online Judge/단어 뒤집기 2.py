def reverseString(s):
    arr = []
    answer = ''
    check = False
    
    for ch in s:
        if ch == '>': 
            answer += '>'
            check = False
        elif ch == '<':
            if arr:
                while arr:
                    answer += arr.pop()
            answer += '<'
            check = True
        elif check:
            answer += ch
        elif ch == ' ':
            while arr:
                answer += arr.pop()
            answer += ch
        else:
            arr.append(ch)
                
    while arr:
        answer += arr.pop()
          
    return answer
    
s = input()
print(reverseString(s))