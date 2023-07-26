# 알고리즘 교육 받을때 LCA 문제가 있어서 배웠다.
# 무려 플레 문제를 냈을줄이야..

import sys
from collections import deque
from math import log2

# node1과 node2의 최소공통조상을 찾는다.
# 이때 depth를 올라갈때 1씩 올라가는 것이 아니라 2^k 씩 올라간다.
def find_lca(node1, node2):
    # node2가 더 깊이가 깊도록 만들어 준다.
    if depth[node1] > depth[node2]:
        node1, node2 = node2, node1

    max_k = int(log2(depth[node2]))

    # node2를 node1의 depth까지 올린다.
    for k in range(max_k, -1, -1):
        if depth[parent[node2][k]] >= depth[node1]:
            node2 = parent[node2][k]

    # node1과 node2의 깊이를 맞췄더니 같다면 node1이 공통조상인 것이므로 node1을 반환한다.
    if node1 == node2:
        return node1

    # 두 노드의 공통조상 바로 밑의 depth까지 올린다.
    max_k = int(log2(depth[node2]))
    for k in range(max_k, -1, -1):
        if parent[node1][k] != parent[node2][k]:
            node1 = parent[node1][k]
            node2 = parent[node2][k]

    # 두 노드의 공통조상 바로 밑의 노드이므로, 부모 노드를 반환한다.
    return parent[node1][0]


N = int(input())
adj_list = [[] for _ in range(N+1)]

# parent[i][k]는 i의 2^k 번째 부모를 의미한다.
parent = [[1]*18 for _ in range(N+1)]
depth = [0] * (N+1)
max_depth = 0
answer = []

queue = deque()
visited = [False] * (N+1)

# 인접 리스트
for _ in range(N-1):
    i, j = map(int, sys.stdin.readline().split())
    adj_list[i].append(j)
    adj_list[j].append(i)

# bfs를 돌며 부모, depth 정보를 업데이트 한다.
queue.append(1)
visited[1] = True

while queue:
    node = queue.popleft()

    for next in adj_list[node]:
        if not visited[next]:
            parent[next][0] = node
            depth[next] = depth[node] + 1
            max_depth = max(max_depth, depth[next])

            visited[next] = True
            queue.append(next)

# parent를 계산해서 구한다. 여기서 int(log2(max_depth))+1 는 최대 k를 의미한다.
for k in range(1, int(log2(max_depth))+1):
    for i in range(1, N+1):
        # 2^k 번째 부모는 2^k-1 번째 부모의 2^k-1 번째 부모이다.
        parent[i][k] = parent[parent[i][k-1]][k-1]

M = int(input())

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    answer.append(find_lca(a, b))

print(*answer)
