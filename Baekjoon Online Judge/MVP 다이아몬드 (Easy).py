N = int(input())
s, g, p, d = map(int, input().split())
player = input()

sum_money = 0
prev = 0

for i in range(N):
    if player[i] == 'B':
        sum_money += s - 1 - prev
        prev = s - 1 - prev 
    elif player[i] == 'S':
        sum_money += g - 1 - prev
        prev = g - 1 - prev
    elif player[i] == 'G':
        sum_money += p - 1 - prev
        prev = p - 1 - prev
    elif player[i] == 'P':
        sum_money += d - 1 - prev
        prev = d - 1 - prev    
    elif player[i] == 'D':
        sum_money += d
        prev = d
    
print(sum_money)