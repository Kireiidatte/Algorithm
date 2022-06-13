numbers = {'c': 26, 'd':10}
s = input()

ans = numbers[s[0]]

for i in range(1, len(s)):
    mul = numbers[s[i]]
    if s[i] == s[i - 1]:
        mul -= 1
    ans *= mul

print(ans)