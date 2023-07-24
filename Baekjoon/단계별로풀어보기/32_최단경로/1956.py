# pypy3로 제출시 속도에서 전체 2등을 했다!!
# heap으로 구현한 다익스트라에 백트래킹을 혼합해서 구현했다.

from heapq import heappop, heappush
import sys

V, E = map(int, input().split())

# 가중치 행렬
W = [[sys.maxsize] * (V+1) for _ in range(V+1)]
# 인접 리스트
adj_list = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())

    W[a][b] = c
    adj_list[a].append([c, b])

min_cycle = sys.maxsize

# start 노드를 시작으로 하는 사이클 중 최소 사이클을 찾는다.
# 이때 다익스트라와 백트래킹을 혼합하여 빠르게 찾는다.
def get_min_cycle(start):
    global min_cycle
    # 최소 힙으로 start 노드로부터의 거리가 짧은 순으로 정렬된다.
    heap = []

    # start 노드로부터의 거리를 저장한다. 계속 업데이트 된다.
    cur_dist = [sys.maxsize] * (V+1)
    visited = [False] * (V+1)

    # start 노드와 연결된 노드들 중 거리가 min_cycle 보다 작은 노드들만 힙에 넣는다.
    for dist_j, j in adj_list[start]:
        if dist_j < min_cycle:
            cur_dist[j] = dist_j
            heappush(heap, (dist_j, j))

    # heap이 빌때까지 반복한다.
    while heap:
        dist_i, i = heappop(heap)

        # heap에서 꺼낸 가장 작은 거리가 min_cycle 보다 작다면, 더이상 min_cycle 보다 작은 사이클을 찾을 수 없다는 것이다.
        # 따라서 함수를 종료한다.
        if dist_i >= min_cycle:
            return

        # heap에서 꺼낸 노드를 이미 방문했다면(즉 노드 i까지의 거리가 이미 업데이트 되었다면) pass한다.
        if visited[i]:
            continue

        # heap에서 꺼낸 노드에서 start 노드로 가는 edge가 있다면, 해당 경로는 사이클이 된다.
        # 해당 사이클의 거리가 min_cycle 보다 작다면 업데이트 해준다.
        if W[i][start] != sys.maxsize:
            min_cycle = min(min_cycle, dist_i + W[i][start])

        visited[i] = True

        # heap에서 꺼낸 노드를 경유해서 가는 경로가 기존 경로보다 빠르다면 업데이트 한다.
        # 이때 해당 경로가 min_cycle 보다 작은 경우에만 업데이트하고, heap에 넣는다.
        for dist_j, j in adj_list[i]:
            if not visited[j] and dist_i + dist_j < min(min_cycle, cur_dist[j]):
                cur_dist[j] = dist_i + dist_j
                heappush(heap, (dist_i + dist_j, j))


# 각 노드를 시작 노드로 했을때 최단 사이클이 있는지 찾는다.
for start in range(1, V+1):
    get_min_cycle(start)

# 만약 없다면 -1을 출력한다.
if min_cycle == sys.maxsize:
    min_cycle = -1

print(min_cycle)
