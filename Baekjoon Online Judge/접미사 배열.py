S = input()
arr = []

for i in range(1, len(S)+1):
    arr.append(S[-i:])

arr.sort()
for a in arr:
    print(a)
