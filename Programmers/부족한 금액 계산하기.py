def solution(price, money, count):
    total_money = 0
    
    for i in range(1, count + 1):
        total_money += i * price
    
    answer = total_money - money
    
    return 0 if answer < 0 else answer