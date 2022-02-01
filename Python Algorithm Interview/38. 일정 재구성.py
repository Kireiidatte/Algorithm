from collections import defaultdict

def findItinerary(tickets):
    graph = defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)
    print(graph)
    route = []
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)
    
    dfs('JFK')
    
    return route[::-1]
