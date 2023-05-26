import sys
from collections import Counter

N = int(input())
cards = Counter(list(map(int, sys.stdin.readline().split())))
M = int(input())
nums = list(map(int, sys.stdin.readline().split()))

for num in nums:
    print(cards[num], end=' ')