import collections

def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    deq_A = collections.deque(A)
    deq_B = collections.deque(B)
    
    while deq_A:
        answer += deq_A.popleft() * deq_B.pop()
      
    return answer