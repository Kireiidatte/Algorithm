def get_notation(n, k):
    converted_num = ''
    
    while n > 0:
        n, mod = divmod(n, k)
        converted_num += str(mod)
    converted_num = converted_num[::-1]
    
    return converted_num

def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    
    return True

def solution(n, k):
    answer = 0
    converted_num = get_notation(n, k)
    
    lst = converted_num.split('0')    
    
    for num in lst:
        if len(num) > 0:
            if int(num) != 1 and isPrime(int(num)):
                answer += 1
  
    return answer