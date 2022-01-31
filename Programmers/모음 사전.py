# 수학문제
def solution(word):
    start = {'E':1, 'I':2, 'O':3, 'U':4}
    result = 0

    for i in range(len(word)):
        if word[i] == 'A':
            result += 1
        else:
            for j in range(4, i, -1):
                result += (5 ** (j - i)) * start[word[i]]
            result += start[word[i]] + 1
    
    return result

