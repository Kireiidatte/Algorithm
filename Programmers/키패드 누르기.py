def solution(numbers, hand):
    answer = ''
    coor = {0:[3,1], 1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], '*': [3,0], '#':[3,2]}
    L = ['*']
    R = ['#']
    
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            L.append(num)
        elif num in [3, 6, 9]:
            answer += 'R'
            R.append(num)
        else:
            LDist = abs(coor[num][0] - coor[L[-1]][0]) + abs(coor[num][1] - coor[L[-1]][1]) 
            RDist = abs(coor[num][0] - coor[R[-1]][0]) + abs(coor[num][1] - coor[R[-1]][1]) 
            if LDist > RDist:
                answer += 'R'
                R.append(num)
            elif LDist < RDist:
                answer += 'L'
                L.append(num)
            elif LDist == RDist:
                if hand == 'right':
                    answer += 'R'
                    R.append(num)
                else:
                    answer += 'L'
                    L.append(num)
                
    return answer
