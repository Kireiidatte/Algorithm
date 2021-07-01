def solution(n, words):
    cnt = 1
    num = 2
    answer = []
    
    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][-1] or words[i] in words[:i]:    break
        else:
            num += 1
            if num > n:    num = 1
            if (i + 1) % n == 0:
                cnt += 1
        
        if i == len(words) - 1:
            return [0, 0]
        
    answer.append(num)
    answer.append(cnt)

    return answer