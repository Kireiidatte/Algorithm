import heapq

def solution(jobs):
    answer, time, i = 0, 0, 0
    start = -1
    heap = []
    
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= time:
                heapq.heappush(heap, [job[1], job[0]])
        if heap:
            job = heapq.heappop(heap)
            start = time
            time += job[0]
            answer += time - job[1]
            i += 1
        else:
            time += 1
    
    return answer // len(jobs)
            