import math

def solution(n,a,b):
    answer = 0

    while True:
        answer += 1
        
        if b > a and b % 2 == 0:
            if b == a + 1:
                break
        elif b < a and a % 2 == 0:
            if a == b + 1:
                break
        
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)

    return answer