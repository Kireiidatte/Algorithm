import collections

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    runtime = 0
    cache = collections.deque()
    
    for city in cities:
        city = city.lower()
        
        if city not in cache:
            runtime += 5
        else:
            runtime += 1
            cache.remove(city)
        cache.append(city)
        
        if len(cache) > cacheSize:
            cache.popleft()
    
    return runtime