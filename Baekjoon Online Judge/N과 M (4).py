from itertools import combinations_with_replacement

n, m = map(int, input().split())

num_list = [i+1 for i in range(n)]
num_list = list(combinations_with_replacement(num_list, m))

for num in num_list:
    for i in range(len(num)):
        print(num[i], end=' ')
    print()
