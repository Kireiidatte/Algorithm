from itertools import combinations
from collections import deque

def solution(relation):
    n = len(relation)
    m = len(relation[0])
    answer = 0
        
    com = []
    for i in range(1, m + 1):
        com.extend(list(combinations(range(m), i)))
    
    keys = deque()
    for idx in com:
        
    
    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))

'''
100  ryan   music    2
200 apeach  math     2
300  tube   computer 3
400  con    computer 4
500  muzi   music    3
600  apeach music    2
'''

