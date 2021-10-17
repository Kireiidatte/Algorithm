def check(arr):
    n=len(arr)
    answer=1

    for i in range(n):
        cnt=1
        
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt=1
            if cnt > answer:
                answer = cnt

        cnt=1
        
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt=1
            if cnt > answer:
                answer = cnt

    return answer

n = int(input())
a = []
max_candy = 0

for _ in range(n):
    a.append(list(input()))

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            a[i][j], a[i][j+1] = a[i][j+1], a[i][j]
            tmp = check(a)
            if tmp > max_candy:
                max_candy = tmp
            a[i][j], a[i][j+1] = a[i][j+1], a[i][j]
        
        if i + 1 < n:
            a[i][j], a[i+1][j] = a[i+1][j], a[i][j]
            tmp = check(a)
            if tmp > max_candy:
                max_candy = tmp
            a[i][j], a[i+1][j] = a[i+1][j], a[i][j]
        
print(max_candy)