from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(list)
    
    for i, j in clothes:
        clothes_dict[j].append(i)
    
    for key in clothes_dict.keys():
        answer *= len(clothes_dict[key]) + 1

    return answer-1