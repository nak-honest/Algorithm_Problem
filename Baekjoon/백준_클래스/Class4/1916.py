# 걸린 시간 : 10분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

import sys
from heapq import heappush
from heapq import heappop

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, c = map(int, sys.stdin.readline().split())
    graph[u].append([c, v])

A, B = map(int, input().split())

dist = [sys.maxsize for _ in range(N+1)]
dist[A] = 0
heap = []
heappush(heap, (0, A))

while heap:
    cost, node = heappop(heap)
    if cost > dist[node]:
        continue
    if node == B:
        print(cost)
        break

    for next_cost, next_node in graph[node]:
        if dist[next_node] > cost + next_cost:
            dist[next_node] = cost + next_cost
            heappush(heap, (dist[next_node], next_node))

