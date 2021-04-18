import math
from itertools import permutations

def isPrime(num):
    if num <= 1: return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def findingPrime(numbers):
    answer = 0
    lst = []
    for i in range(1, len(numbers) + 1):
        permute = permutations(numbers, i)
        for j in permute:
            tmp = ''.join(j)
            lst.append(int(tmp))

    lst = list(set(lst))
    
    for i in lst:
        if isPrime(i): answer += 1
    
    return answer