import sys
from heapq import heappop, heappush

V, E = map(int, input().split())
K = int(input())

adj_list = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    adj_list[u].append([w, v])


cur_dist = [sys.maxsize] * (V+1)
cur_dist[K] = 0
heap = [[0, K]]
visited = [False] * (V+1)

for w, v in adj_list[K]:
    cur_dist[v] = w
    heappush(heap, [w, v])

while heap:
    w, v = heappop(heap)
    if visited[v]:
        continue

    visited[v] = True

    for new_dist, new_node in adj_list[v]:
        if w + new_dist < cur_dist[new_node]:
            cur_dist[new_node] = new_dist + w
            heappush(heap, [w+new_dist, new_node])


for i in range(1, V+1):
    if cur_dist[i] == sys.maxsize:
        print("INF")
    else:
        print(cur_dist[i])