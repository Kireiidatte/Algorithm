import sys

while True:
    s = sys.stdin.readline().rstrip('\n')
    up, lo, sp, nu = 0, 0, 0, 0
    
    if not s:
        break
            
    for ch in s:
        if ch.islower():
            lo += 1
        elif ch.isupper():
            up += 1
        elif ch.isdigit():
            nu += 1
        elif ch.isspace():
            sp += 1
    
    sys.stdout.write("{} {} {} {}\n".format(lo, up, nu, sp))