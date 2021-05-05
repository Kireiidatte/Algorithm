from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for num in course:
        candidate = []
        for strs in orders:
            for i in combinations(strs, num):
                tmp = ''.join(sorted(i))
                candidate.append(tmp)
        t_candidate = Counter(candidate).most_common()
        answer += [menu for menu, cnt in t_candidate if cnt > 1 and cnt == t_candidate[0][1]]
    
    return sorted(answer)