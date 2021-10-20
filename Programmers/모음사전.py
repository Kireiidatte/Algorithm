# 수학문제
def solution(word):
    start = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    result = 0
    word_length = len(word)
    result += start[word[0]]
    
    if word_length == word.count(word[0]):
        return result + word.count(word[0]) - 1
    
    
    
    return result