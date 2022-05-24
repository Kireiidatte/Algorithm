score = {4:'E', 3:'A', 2: 'B', 1:'C', 0:'D'}

for _ in range(3):
    lst = [*map(int, input().split())]
    print(score[sum(lst)])


