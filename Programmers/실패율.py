def solution(N, stages):
    answer = []
    stages.sort()
    
    for i in range(1, N+1):
        fail = 0

        if len(stages) == 0:
            answer.append([i, 0])
        else:
            for j in range(len(stages)):
                if stages[j] == i:
                    fail += 1
                else:
                    break
            answer.append([i, fail/len(stages)])
            
            for _ in range(fail):
                stages.pop(0)
    
    answer.sort(key=lambda x: (-x[1], x[0]))
    
    return [i[0] for i in answer]