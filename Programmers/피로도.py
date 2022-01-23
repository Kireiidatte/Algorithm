from itertools import permutations

def solution(k, dungeons):
    answer = 0

    idx = []
    for i in range(len(dungeons)):
        idx.append(i)
    idx = list(permutations(idx, len(dungeons)))

    for i in idx:
        cur_k = k
        tmp = 0
        for j in i:
            if dungeons[j][0] > cur_k:
                break
            elif dungeons[j][0] <= cur_k:
                cur_k -= dungeons[j][1]
                tmp += 1
        
        answer = max(tmp, answer)
    
    return answer
