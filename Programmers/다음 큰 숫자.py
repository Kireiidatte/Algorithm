def solution(n):
    count1 = bin(n).count('1')
    num = n
   
    while(True):
        num += 1
        if bin(num).count('1') == count1:
            break
        
    return num

print(solution(15))