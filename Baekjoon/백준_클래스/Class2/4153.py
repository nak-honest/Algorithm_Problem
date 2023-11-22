from heapq import nsmallest
import sys

while True:
    lines = list(map(int, sys.stdin.readline().split()))
    if sum(lines) == 0:
        break

    a, b = nsmallest(2, lines)
    c = max(lines)

    print(["wrong", "right"][int((a ** 2 + b ** 2) == c ** 2)])