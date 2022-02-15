from collections import defaultdict

def solution(genres, plays):
    answer = []
    # 장르별 플레이 합산 저장
    plays_genre = defaultdict(int)
    # 곡 인덱스 저장
    idx_genre = defaultdict(lambda: [])
    
    for i in range(len(genres)):
        plays_genre[genres[i]] += plays[i]
        idx_genre[genres[i]].append((plays[i] ,i))
    # plays_genre 값을 value 기준으로 내림차순 정렬
    plays_genre = sorted(plays_genre.items(), key = lambda x: -x[1])
    # idx_genre값을 key 기준으로 내림차순 정렬, 장르 내 재생 횟수가 같은 경우 오름차순 정렬
    for key in idx_genre.keys():
        idx_genre[key].sort(key = lambda x:(-x[0], x[1]))
    
    for i in range(len(plays_genre)):
        if len(idx_genre[plays_genre[i][0]]) == 1:
            answer.append(idx_genre[plays_genre[i][0]][0][1])
        else:
            for j in range(2):
                answer.append(idx_genre[plays_genre[i][0]][j][1])
    
    return answer