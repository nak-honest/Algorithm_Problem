import sys
from heapq import heappop, heappush

# sys.maxsize에 더하기 연산을 적용하면, 오버플로우가 발생하기 때문에 따로 함수로 뺀다.
def add_dist(i, j):
    if i == sys.maxsize or j == sys.maxsize:
        return sys.maxsize
    return i + j

# heap으로 구현한 다익스트라를 이용해 start -> end 의 최단 거리를 구해서 반환한다. 경로가 없을시 sys.maxsize가 반환된다.
def dijkstra(adj, start, end):
    heap = []
    cur_dist = [sys.maxsize] * len(adj)
    visited = [False] * len(adj)

    cur_dist[start] = 0
    heap.append((0, start))

    while heap:
        dist, node = heappop(heap)
        if visited[node]:
            continue

        if node == end:
            break

        visited[node] = True

        for next_dist, next in adj[node]:
            if not visited[next] and add_dist(cur_dist[node], next_dist) < cur_dist[next]:
                cur_dist[next] = add_dist(cur_dist[node], next_dist)
                heappush(heap, (cur_dist[next], next))

    return cur_dist[end]


N, E = map(int, input().split())
adj_list = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    adj_list[a].append([c, b])
    adj_list[b].append([c, a])

v1, v2 = map(int, input().split())

# 최단 경로는 1 -> v1 -> v2 -> N 또는 1 -> v2 -> v1 -> N 중 하나이다. 그 중 최솟값이 최단 경로이다.
answer = min(add_dist(add_dist(dijkstra(adj_list, 1, v1), dijkstra(adj_list, v1, v2)), dijkstra(adj_list, v2, N)),
             add_dist(add_dist(dijkstra(adj_list, 1, v2), dijkstra(adj_list, v2, v1)), dijkstra(adj_list, v1, N)))

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
