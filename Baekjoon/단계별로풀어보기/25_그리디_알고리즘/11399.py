import heapq
import sys

N = int(input())
P = list(map(int, sys.stdin.readline().split()))

heapq.heapify(P)

cur_time = 0
total_time = 0

for _ in range(N):
    cur_time += heapq.heappop(P)
    total_time += cur_time

print(total_time)