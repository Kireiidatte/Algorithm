# 현재 시간을 밀리초로 바꾸는 함수
def getTime(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:8])
    millisecond = int(time[9:])
    
    return (hour + minute + second) * 1000 + millisecond
# 처리 시작 시간을 구하는 함수
def getStartTime(time, duration):
    d = duration[:-1]
    d_time = int(float(d) * 1000)
    return getTime(time) - d_time + 1

def solution(lines):
    answer = 0
    start_time = []
    end_time = []
    
    for i in lines:
        time = i.split(' ')
        start_time.append(getStartTime(time[1], time[2]))
        end_time.append(getTime(time[1]))
    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i]
        for j in range(i, len(lines)):
            if cur_end_time > start_time[j] - 1000:
                cnt += 1
        answer = max(answer, cnt)
    
    return answer