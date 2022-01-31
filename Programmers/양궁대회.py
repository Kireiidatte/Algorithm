from itertools import combinations_with_replacement

def getLowScore(info1, info2):
    for i in range(len(info1)):
        if info1[10-i] == info2[10-i]:
            continue
        elif info1[10-i] > info2[10-i]:
            return info1
        else:
            return info2
        
def solution(n, info):
    answer = [0] * 11
    max_diff = 0
    
    for comb in combinations_with_replacement(range(11), n):
        tmp = [0] * 11
        tmp_diff = 0
        tmp_sum, a_sum = 0, 0
        
        for c in comb:
            tmp[c] += 1    
        
        for i in range(len(tmp)):
            if tmp[i] == 0 and info[i] == 0:
                continue
            elif tmp[i] > info[i]:
                tmp_sum += 10 - i
            else:
                a_sum += 10 - i
        
        tmp_diff = tmp_sum - a_sum
        
        if tmp_diff > 0:
            if tmp_diff > max_diff:
                answer = tmp
                max_diff = tmp_diff
            elif tmp_diff == max_diff:
                answer = getLowScore(answer, tmp)
        
    if sum(answer) == 0:
        return [-1]
    else:
        return answer