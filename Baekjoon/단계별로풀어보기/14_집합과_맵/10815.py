import sys
N = int(input())
cards = dict.fromkeys(map(int, sys.stdin.readline().split()), 0)
M = int(input())
nums = list(map(int, sys.stdin.readline().split()))

for num in nums:
    print(int(num in cards), end=' ')