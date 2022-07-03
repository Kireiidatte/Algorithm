import sys
from itertools import combinations

N, M = map(int, input().split())
city = [[*map(int, input().split())] for _ in range(N)]

house = []
chicken = []
result = sys.maxsize

for i in range(N):
    for j in range(N):
        # 집일 경우
        if city[i][j] == 1:
            house.append([i, j])
        # 치킨집일 경우
        elif city[i][j] == 2:
            chicken.append([i, j])
    
for c in combinations(chicken, M):
    tmp = 0
    
    for h in house:
        # 각 집마다 치킨 거리
        chicken_length = sys.maxsize
        for i in range(M):
            chicken_length = min(chicken_length, abs(h[0] - c[i][0]) + abs(h[1] - c[i][1]))
        tmp += chicken_length
    
    result = min(result, tmp)

print(result)   