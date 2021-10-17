a = []

for i in range(9):
    a.append(int(input()))

a.sort()
    
for i in range(len(a) - 1):
    for j in range(i+1, len(a)):
        if sum(a) - a[i] - a[j] == 100:
            a = a[:i] + a[i+1:j] + a[j+1:]
            break
    if len(a) == 7:
        break

for i in a:
    print(i)

