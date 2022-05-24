hour, minute = map(int, input().split())

if minute >= 45:
    print('{0} {1}'.format(hour, minute-45))
else:
    if hour == 0:
        print('{0} {1}'.format(23, 15+minute))    
    else:
        print('{0} {1}'.format(hour-1, 15+minute))
