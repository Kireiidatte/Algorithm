import collections

def solution(clothes):
    answer = 1
    clothes_dict = collections.defaultdict(list)
   
    for i, j in clothes:
        clothes_dict[j].append(i)
    
    for i in clothes_dict.keys():
        answer *= len(clothes_dict[i]) + 1
    
    return answer - 1