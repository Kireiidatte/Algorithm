# 신호등 개수, 도로의 길이
N, L = map(int, input().split())
# 신호등 위치
traffic_lights = {}
# 시작 위치
cur_loc = 0
# 걸리는 시간
time = 0
# 신호등 위치, 빨간색 지속 시간, 초록색 지속 시간
for _ in range(N): 
    d, r, g = map(int, input().split())
    traffic_lights[d] = (r, g)

while True:
    # 도로의 길이에 다다르면 break
    if cur_loc == L:    break
    # 신호등이 존재하지 않는 경우
    if traffic_lights.get(cur_loc) is None:
        cur_loc += 1
        time += 1
    else:
        red, green = traffic_lights[cur_loc]
        tmp = time % (red + green)
        # 신호등에 걸리는 경우 기다림
        if tmp < red:
            time += (red - tmp + 1)
            cur_loc += 1
        # 신호등에 걸리지 않는 경우 패스
        else:
            cur_loc += 1
            time += 1
        
print(time)
