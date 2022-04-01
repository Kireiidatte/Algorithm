num_dic = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

def get_notation(n, size):
    total = '0'
    for i in range(1, size+1):
        tmp = ''
        while i > 0:
            i, mod = divmod(i, n)
            if mod >= 10:
                tmp += num_dic[mod]
            else:
                tmp += str(mod)
        total += tmp[::-1]
    
    return total

def solution(n, t, m, p):
    answer = ''
    total = get_notation(n, m*t)
    
    for i in range(p-1, len(total), m):
        if len(answer) == t:
            break
        answer += total[i]    
    
    return answer