def solution(record):
    answer = []
    record = [i.split(' ') for i in record]
    name  = {}
    
    for log in record:
        if log[0] != 'Leave':
            name[log[1]] = log[2]
    
    for log in record:
        if log[0] == 'Enter':
            answer.append(name[log[1]] + '님이 들어왔습니다.')
        elif log[0] == 'Leave':
            answer.append(name[log[1]] + '님이 나갔습니다.')
            
    return answer

