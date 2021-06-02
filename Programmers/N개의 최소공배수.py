def solution(arr):
    def gcd(a, b):
        if b > a:
            tmp = a
            a = b
            b = tmp
        while b > 0:
            c = b
            b = a % b
            a = c
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    
    if len(arr) == 1:
        return arr[0]
    
    answer = lcm(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        answer = lcm(answer, arr[i])
        
    return answer
