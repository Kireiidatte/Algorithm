from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    info_dict = {}

    for i in info:
        tmp = i.split(' ')
        key = tmp[:-1]
        value = tmp[-1]

        for j in range(len(i)):
            for c in combinations(key, j):
                tmp = ''.join(c) 
                if tmp in info_dict:
                    info_dict[tmp].append(int(value))
                else:
                    info_dict[tmp] = [int(value)]
        
    for i in info_dict:
        info_dict[i].sort()
    
    for q in query:
        query_split = q.split(' and ')
        for i in query_split.pop().split(' '):
            query_split.append(i)
        
        q_key = query_split[:-1]
        q_val = query_split[-1]
        
        while '-' in q_key:
            q_key.remove('-')
        q_key = ''.join(q_key)

        if q_key in info_dict:
            score = info_dict[q_key]
            if score:
                idx = bisect_left(score, int(q_val))
                answer.append(len(score) - idx)
        else:
            answer.append(0)      
    
    return answer