import heapq

def solution(N, road, K):
    answer = 0
    distance = [float('inf')] * (N+1)
    graph =  [[] for i in range(N+1)]

    for i in road:
        graph[i[0]].append((i[1], i[2]))
        graph[i[1]].append((i[0], i[2]))

    def dijkstra(start):
        q = []
        heapq.heappush(q, (start, 0))
        distance[start] = 0
        
        while q:
            now, dist = heapq.heappop(q)
        
            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (i[0], cost))


    dijkstra(1)

    for i in range(1, len(distance)):
        if distance[i] <=  K:
            answer += 1 

    return answer