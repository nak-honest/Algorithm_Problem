# 문제를 잘 읽자 ^^ A -> B 경로가 중복되지 않는다는 말은 어디에도 없다 ㅋㅎ..

import sys
from heapq import heappop, heappush

def add(node1, node2):
    if node1 == sys.maxsize or node2 == sys.maxsize:
        return sys.maxsize

    return node1 + node2

n = int(input())
m = int(input())
adj_list = [[] for _ in range(n+1)]
W = [[sys.maxsize] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    W[i][i] = 0

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    if v not in adj_list[u]:
        adj_list[u].append(v)
    W[u][v] = min(w, W[u][v])

a, b = map(int, input().split())

# 힙으로 구현한 다익스트라를 통해 A -> B로 가는 최단 경로를 구한다.

visited = [False] * (n+1)
prev = [-1] * (n+1)
cur_dist = [sys.maxsize] * (n+1)
cur_dist[a] = 0

heap = [[0, a, -1]]

while heap:
    dist, node, p = heappop(heap)

    if visited[node]:
        continue

    # 이전 노드 정보를 업데이트 해서 역추적 할 수 있게 한다.
    prev[node] = p

    if node == b:
        break

    visited[node] = True

    for next in adj_list[node]:
        if not visited[next] and add(dist, W[node][next]) < cur_dist[next]:
            cur_dist[next] = dist + W[node][next]
            heappush(heap, [cur_dist[next], next, node])

answer = []
cur = b

while cur != -1:
    answer.append(cur)
    cur = prev[cur]

print(cur_dist[b])

print(len(answer))

print(*reversed(answer))
