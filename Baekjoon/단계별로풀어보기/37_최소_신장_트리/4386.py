# 걸린 시간 : 17분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

# 크루스칼 알고리즘으로 별자리를 만드는데 필요한 최소 비용을 구한다.
import sys
from heapq import heappop, heappush

def get_dist(pair1, pair2):
    return ((pair1[0] - pair2[0]) ** 2 + (pair1[1] - pair2[1]) ** 2) ** 0.5

def find_root(node):
    while node != union[node]:
        node = union[node]

    return node

n = int(input())
nodes = []

for _ in range(n):
    x, y = map(float, sys.stdin.readline().split())
    nodes.append((x, y))

# 모든 노드간의 에지를 구해서 거리에 대해 최소 힙을 구성한다.
edges = []

for i in range(n):
    for j in range(i+1, n):
        dist = get_dist(nodes[i], nodes[j])
        heappush(edges, [dist, i, j])

union = [i for i in range(n)]
depth = [0 for _ in range(n)]

total_cost = 0
count = 0

while count != n-1:
    # 비용이 최소인 에지를 꺼낸다. 해당 에지가 이미 그래프에 포함되어있다면 다음 에지를 확인한다.
    dist, i, j = heappop(edges)
    root_i = find_root(i)
    root_j = find_root(j)

    if root_i == root_j:
        continue

    count += 1
    total_cost += dist

    if depth[root_i] > depth[root_j]:
        union[root_j] = root_i
    elif depth[root_i] < depth[root_j]:
        union[root_i] = root_j
    else:
        union[root_j] = root_i
        depth[root_i] += 1

print(total_cost)
