import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    works = [-i for i in works]
    heapq.heapify(works)
    
    while n:
        w = heapq.heappop(works) + 1
        heapq.heappush(works, w)
        n -= 1
    
    return sum([i*i for i in works])
