import sys

# sys.stdin.readline() 사용해야함
N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

for i in sorted(nums):
    print(i)