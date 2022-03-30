from collections import Counter
S = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
counter = Counter(S)

for ch in alphabet:
    if counter[ch]:
        print(counter[ch], end=' ')
    else:
        print(0, end=' ')
