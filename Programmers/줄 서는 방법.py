import math

def solution(n, k):
    answer = []
    nums = [i for i in range(1, n+1)]

    while nums:
        tmp = math.factorial(n-1)
        q, r = divmod(k, tmp)
        
        if r == 0:
            q -= 1
        
        answer.append(nums.pop(q))

        n -= 1
        k = r

    return answer

