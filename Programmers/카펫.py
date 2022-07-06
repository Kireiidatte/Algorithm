import math 

def get_divisor(total):
    lst = []
    
    for i in range(3, int(math.sqrt(total)) + 1):
        if total % i == 0:
            lst.append(i)
    
    return lst

def solution(brown, yellow):
    answer = []
    size = brown + yellow
    divisors = get_divisor(size)
    
    width, height = 0, 0
    
    for divisor in divisors:
        width, height = size / divisor, divisor
        if 2*width + 2*height == brown + 4:
            return width, height