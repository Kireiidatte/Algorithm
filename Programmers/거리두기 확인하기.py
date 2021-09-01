from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(place, person):
    visited = [[False] * 5 for _ in range(5)]
    cnt = 0
    q = deque()
    q.append(person)
    
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            visited[x][y] = True
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= 5 or ny >= 5  or visited[nx][ny]: 
                    continue
                if place[nx][ny] == 'P':
                    return False
                elif place[nx][ny] == 'X':
                    continue
                else:
                    q.append((nx, ny))
                    
        cnt += 1
        if cnt == 2 or not q:
            return True

def solution(places):
    answer = []
    
    for place in places:
        people = deque()
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append((i, j))
                    
        if len(people) == 0:
            answer.append(1)
            continue
    
        flag = True
        
        for person in people:
            if not bfs(place, person):
                flag = False
                break
    
        if not flag:
            answer.append(0)
        else:
            answer.append(1)
            
    return answer