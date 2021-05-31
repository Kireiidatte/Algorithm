def solution(dirs):
    cmd = {'U' : (0, 1), 'D' : (0, -1), 'L' : (-1, 0), 'R' : (1, 0)}
    route = set()
    cur_x, cur_y = (0, 0)
    
    for i in dirs:
        d_x, d_y = cur_x + cmd[i][0], cur_y + cmd[i][1]
        
        if -5 <= d_x <= 5 and -5 <= d_y <= 5:
            route.add((cur_x, cur_y, d_x, d_y))
            route.add((d_x, d_y, cur_x, cur_y))
            cur_x, cur_y = d_x, d_y
    
    return len(route) / 2
