from collections import defaultdict

def solution(str1, str2):
    set1 = defaultdict(int)
    set2 = defaultdict(int)
    
    for i in range(len(str1) - 1):
        if str1[i:i+2].isalpha():
            set1[str1[i:i+2].lower()] += 1
            
    for i in range(len(str2) - 1):
        if str2[i:i+2].isalpha():
            set2[str2[i:i+2].lower()] += 1
    
    intersection = 0
    union = 0
    
    for elem in set1:
        if elem in set2:
            intersection += min(set1[elem], set2[elem])
            union += max(set1[elem], set2[elem])
        else:
            union += set1[elem]
    
    for elem in set2:
        if elem not in set1:
            union += set2[elem]
                
    if intersection == 0 and union == 0:
            jaccard_sim = 1
    else:
        jaccard_sim = intersection / union 
    
    return int(jaccard_sim * 65536)
