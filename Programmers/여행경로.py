from collections import defaultdict

def solution(tickets):
    answer = []
    tickets.sort(reverse = True)
    
    dic = defaultdict(list)
    for t1, t2 in tickets:
        dic[t1].append(t2)
    
    stack = ['ICN']
    
    while stack:
        now = stack[-1]
        if not now in dic or len(dic[now]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(dic[now].pop())
        
    answer.reverse()
    
    return answer