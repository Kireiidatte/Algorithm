from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    comb = []
    for i in range(1, col + 1):
        comb.extend(combinations(range(col), i))
    
    unique = []
    for c in comb:
        ### 문자열, 숫자, 튜플만 set에 넣으면 중복 제거 가능
        tmp = [tuple([item[i] for i in c]) for item in relation]
        
        # 유일성 만족여부 검사
        if len(set(tmp)) == row:
            flag = True
            
            # 최소성 만족여부 검사
            for x in unique:
                if set(x).issubset(set(c)):
                    flag = False
                    break
                    
            if flag: unique.append(c)
        
    return len(unique)