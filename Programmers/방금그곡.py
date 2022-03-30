change = {'C#':'H', 'D#':'I', 'F#':'J', 'A#':'K', 'G#':'L', 'E#':'M', 'B#':'N'}
# 문자열 처리
def change_score(score):
    j = 0
    new_score = ''
    
    while j < len(score):
        if j+1 < len(score) and score[j+1] == '#':
            new_score += change[score[j] + score[j+1]]
            j += 2
        else:
            new_score += score[j]
            j += 1
    
    return new_score

def solution(m, musicinfos):
    answer = ''
    m = change_score(m)
    correct_list = []
    for i in range(len(musicinfos)):
        info = musicinfos[i].split(',')
        new_score = change_score(info[3])
        # 재생시간 계산
        hour = (int(info[1][:2]) - int(info[0][:2])) * 60
        minute = int(info[1][3:]) - int(info[0][3:])
        
        play_time = hour + minute
        tmp = play_time
        plays = ''
        
        # 재생시간이 음악 길이보다 큰 경우 => 음악 반복
        if tmp > len(new_score):
            while True:
                if tmp < len(new_score):
                    plays += new_score[:tmp]
                    break
                plays += new_score
                tmp -= len(new_score)
        # 재생시간이 음악 길이보다 작은 경우 => 해당 길이만큼만 음악 재생
        else:
            plays = new_score[:play_time]
        
        if m in plays:
            correct_list.append([play_time, i, info[2]])
    
    correct_list.sort(key=lambda x : (-x[0], x[1]))
    
    if correct_list:
        return correct_list[0][2]
    else:
        return '(None)'