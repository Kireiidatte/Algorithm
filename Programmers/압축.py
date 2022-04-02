idx = {chr(ord('A')+i):i+1 for i in range(26)}

def solution(msg):
    answer = []
    msg_list = list(msg)[::-1]
    
    while msg_list:
        tmp_in = ''
        tmp_in += msg_list.pop()
        s_idx = max(idx.values()) + 1
        
        while True:
            if len(msg_list) == 0:    break
            elif (tmp_in + msg_list[-1]) in idx:
                tmp_in += msg_list.pop()
            else:
                idx[tmp_in + msg_list[-1]] = s_idx
                s_idx +=1
                break
        
        answer.append(idx[tmp_in])
        
    return answer