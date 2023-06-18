import sys

n = int(input())
max_sum = -1000
current = 0

for num in map(int, sys.stdin.readline().split()):
    current += num
    max_sum = max(max_sum, current)
    if current <= 0:
        current = 0

print(max_sum)