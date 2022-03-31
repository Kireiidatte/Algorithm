A = input().rstrip()
T = input().rstrip()

A = list(A)
reverse_A = list(reversed(A))

left = []
right = []
left_p = 0
right_p = len(T) - 1

flag = True

while left_p <= right_p:
    if flag:
        left.append(T[left_p])
        left_p += 1
        if left[-len(A):] == A:
            left[-len(A):]  = []
            flag = False
    
    else:
        right.append(T[right_p])
        right_p -= 1
        if right[-len(A):] == reverse_A:
            right[-len(A):] = []
            flag = True

while right:
        left.append(right.pop())
        if left[-len(A):] == A:
            left[-len(A):]  = []

answer = ''.join(left)
print(answer)