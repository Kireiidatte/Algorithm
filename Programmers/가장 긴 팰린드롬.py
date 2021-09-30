def isPalindrome(s):
    if s == s[::-1]:
        return True
   
def solution(s):
    maxlen = 0
    
    for i in range(len(s)):
        for j in range(i+1, len(s) + 1):
            if isPalindrome(s[i:j]):
                if maxlen < len(s[i:j]):
                    maxlen = len(s[i:j])

    return maxlen