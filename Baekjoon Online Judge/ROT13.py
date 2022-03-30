S = input()
encrpted = ''

for ch in S:
    if ch.isalpha():
        if ch.isupper():
            encrpted += chr((ord(ch)-65 + 13) % 26 + 65)            
        else:    
            encrpted += chr((ord(ch)-97 + 13) % 26 + 97)
    else:
        encrpted += ch

print(encrpted)
