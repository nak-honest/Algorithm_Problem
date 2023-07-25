import sys
from collections import deque

global depth
global parent

# 선형 탐색 LCA 알고리즘
def LCA(node1, node2):

    # 먼저 두 노드의 depth를 맞춘다.
    while depth[node1] > depth[node2]:
        node1 = parent[node1]

    while depth[node1] < depth[node2]:
        node2 = parent[node2]

    # 두 노드가 같아질때까지 위로 올린다.
    while node1 != node2:
        node1 = parent[node1]
        node2 = parent[node2]

    return node1


T = int(input())

for _ in range(T):
    N = int(input())
    root = 0
    parent = [0 for _ in range(N+1)]
    child = [[] for _ in range(N+1)]
    depth = [0 for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    queue = deque()

    for _ in range(N-1):
        A, B = map(int, sys.stdin.readline().split())
        parent[B] = A
        child[A].append(B)

    # 루트노드를 찾는다.
    for i in range(1, N+1):
        if parent[i] == 0:
            root = i

    visited[root] = True

    for c in child[root]:
        queue.append(c)
        visited[c] = True

    # bfs를 하면서 각 노드의 depth를 업데이트 한다.
    while queue:
        node = queue.popleft()
        depth[node] = depth[parent[node]] + 1

        for c in child[node]:
            if not visited[c]:
                queue.append(c)
                visited[c] = True

    a, b = map(int, input().split())

    print(LCA(a, b))
