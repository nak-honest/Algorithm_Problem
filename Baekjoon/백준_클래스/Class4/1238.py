# 다익스트라를 사용할때 그래프를 adj list로 표현하느냐, 가중치 그래프로 표현하느냐에 따라 시간이 다르다.
# pypy3로는 둘다 통과하지만 python3는 adj list로 표현하는 경우에만 시간초과가 발생하지 않는다.
# 다익스트라를 사용할때 앞으로는 adj list로 풀자!!

# 걸린 시간 : 30분
# 제출 횟수 : 4번
# 풀이 참조 : x
# 반례 참조 : x

import sys
from heapq import heappush
from heapq import heappop

# start 노드에서 X노드로의 최단 거리를 계산한다.
def dijkstra(start):
    heap = []
    d = [sys.maxsize for _ in range(N + 1)]

    heappush(heap, (0, start))

    while heap:
        t, node = heappop(heap)

        if t > d[node]:
            continue

        if node == X:
            return t

        for next_time, next_node in roads[node]:
            if d[next_node] > next_time + t:
                d[next_node] = next_time + t
                heappush(heap, (d[next_node], next_node))



N, M, X = map(int, input().split())
roads = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, T = map(int, sys.stdin.readline().split())
    roads[u].append([T, v])

# X에서 다른 노드까지의 최단 거리를 계산한다.
heap_from_x = []
dist = [sys.maxsize for _ in range(N+1)]

heappush(heap_from_x, (0, X))

while heap_from_x:
    t, node = heappop(heap_from_x)

    if t > dist[node]:
        continue

    for next_time, next_node in roads[node]:
        if dist[next_node] > next_time + t:
            dist[next_node] = next_time + t
            heappush(heap_from_x, (dist[next_node], next_node))

answer = 0
for i in range(1, N+1):
    if i == X:
        continue

    # dijkstra(i) : i에서 X로의 최단거리
    # dist[i] : X에서 i로의 최단거리
    answer = max(answer, dijkstra(i) + dist[i])

print(answer)