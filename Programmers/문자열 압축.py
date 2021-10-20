def solution(s):
    strs = ''
    result = ''
    length = []
    
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s) // 2 + 1):
        cnt = 1
        tmp = s[:i]
        for j in range(i, len(s), i):
            if s[j:j+i] == tmp:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ''
                result += str(cnt) + tmp
                tmp = s[j:j+i]
                cnt = 1
        
        if cnt == 1:
            cnt = ''
        result += str(cnt) + tmp
        length.append(len(result))
        result = ''
    
    return min(length)

""""
먼저 문자열을 몇개 단위로 짜를지에 대해 cut을 이용하는 제일 바깥 for문을 1, len(s) // 2 + 1까지 반복했다. 
문자열을 꼭 2로 나누어 문자열 길이보다 더 넘어가는 비교는 할 필요 없도록 한다. 
그리고 tempStr에 cut만큼 짤라낸 문자열을 대입해 다음 문자열들과 cut 단위로 비교한다.
(s[i:i+cut]) 같으면 count를 +1 해주고, 틀리면 count와 비교했던 tempStr을 result값에 넣어주면 된다. 
그리고 중요한 것이 마지막에 한번 더 result에 count + tempStr을 넣어줘야 제일 마지막으로 비교했던 문자열이 들어갈 수 있다.
"""