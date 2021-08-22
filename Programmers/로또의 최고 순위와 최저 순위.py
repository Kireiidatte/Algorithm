def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    answer = []
    correct = 0
    unknown = 0
    
    for i in lottos:
        if i == 0:
            unknown += 1
        elif i in win_nums:
            correct += 1
    
    answer.append(rank[correct + unknown])
    answer.append(rank[correct])

    return answer