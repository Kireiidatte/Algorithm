# hanoi(N, 시작, 끝, 보조) = hanoi(N-1, 시작, 보조, 끝) + N번만 끝으로 옮기기 + hanoi(N-1, 시작, 끝, 보조)
def hanoi(n, start, end, bypass):
    if n == 1:
        return [[start, end]]
    else:
        path = []
        # hanoi(N-1, 시작, 보조, 끝)
        path += hanoi(n-1, start, bypass, end)
        # N번만 끝으로 옮기기
        path += [[start, end]]
        # hanoi(N-1, 시작, 끝, 보조)
        path += hanoi(n-1, bypass, end, start)
        
        return path

def solution(n):
    answer = hanoi(n, 1, 3, 2)
    return answer