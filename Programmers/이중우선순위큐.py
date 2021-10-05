import heapq

def solution(operations):
    answer = []
    
    heap = []
    
    for op in operations:
        ch, n = op.split()
        if ch == 'I':
            heapq.heappush(heap, int(n))
        if ch == 'D':
            if len(heap) == 0:
                pass
            else:
                if n == '-1':
                    heapq.heappop(heap)
                else:
                    heap = heapq.nlargest(len(heap), heap)[1:]
                    heapq.heapify(heap)
                
    if not heap:
        return [0,0]
    else:
        answer.append(max(heap))
        answer.append(min(heap))
            
    return answer