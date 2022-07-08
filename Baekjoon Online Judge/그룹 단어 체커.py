n = int(input())
words = [input() for _ in range(n)]

cnt = n

for word in words:
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            continue
        elif word[i] in word[i+1:]:
            cnt -= 1
            break

print(cnt)