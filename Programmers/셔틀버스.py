def convert_min(s):
    h, m = s.split(':')
    return int(h) * 60 + int(m)

def convert_string(m):
    h = m // 60
    m = m % 60
    return '{0:02d}:{1:02d}'.format(h, m)

def solution(n, t, m, timetable):
    answer = 0
    times = []
    
    times = [convert_min(time) for time in timetable]
    times.sort()
    
    busTime = [9*60 + t*i for i in range(n)]
    
    idx = 0
    
    for bt in busTime:
        board = 0
        while board < m and idx < len(times) and times[idx] <= bt:
            idx += 1
            board += 1
        if board < m:
            answer = bt
        else:
            answer = times[idx - 1] - 1
      
    return convert_string(answer)