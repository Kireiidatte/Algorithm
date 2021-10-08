from collections import Counter

def largestRight(N, A):
    answer = [-1] * N
    stack = []
    stack.append(0)
    
    counter = Counter(A)
    
    for i in range(1, N):
        while stack and counter[A[stack[-1]]] < counter[A[i]]:
            answer[stack.pop()] = A[i]
        stack.append(i)
    
    print(*answer)

N = int(input())
A = list(map(int, input().split()))
largestRight(N, A)
