def HIndex(citations):
    answer = 0
    citations.sort(reverse = True)
    
    for i in range(len(citations)):
        if citations[i] <= i:    break
        answer += 1
            
    return answer