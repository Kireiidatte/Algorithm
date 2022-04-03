from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    parking_time = defaultdict(int)
    in_time = {}
    
    for record in records:
        tmp = record.split()
        if tmp[2] == 'IN':
            in_time[tmp[1]] = tmp[0]
        else:
            hour = (int(tmp[0][:2]) - int(in_time[tmp[1]][:2])) * 60
            minute = int(tmp[0][3:]) - int(in_time[tmp[1]][3:])
            parking_time[tmp[1]] += hour + minute
            del in_time[tmp[1]]
         
    for key in in_time.keys():
        hour = (23 - int(in_time[key][:2])) * 60
        minute = 59 - int(in_time[key][3:])
        parking_time[key] += hour + minute
    
    parking_time = sorted(parking_time.items())
    
    for p in parking_time:
        if p[1] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] +  math.ceil((p[1] - fees[0]) / fees[2]) * fees[3] )
    
    return answer