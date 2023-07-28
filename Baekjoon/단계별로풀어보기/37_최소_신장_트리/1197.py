# 에지 개수가 노드 개수의 10배밖에 되지 않아서 크러스컬 알고리즘으로 풀었다.

import sys
from heapq import heappop, heapify

V, E = map(int, input().split())

# parent는 서로소 집합에서 각 노드의 부모가 누구인지를 저장한다.
parent = [i for i in range(V+1)]
depth = [0 for _ in range(V+1)]

# 해당 노드가 속한 집합의 루트노드를 찾아서 반환한다.
def find_root(i):
    while parent[i] != i:
        i = parent[i]

    return i

# i가 속한 집합과 j가 속한 집합을 합친다. 이떄 depth가 최대한 증가하지 않도록 한다.
def merge_set(i, j):
    p1 = find_root(i)
    p2 = find_root(j)

    if depth[p1] == depth[p2]:
        depth[p1] += 1
        parent[p2] = p1
    elif depth[p1] > depth[p2]:
        parent[p2] = p1
    else:
        parent[p1] = p2


count = 0
min_weight = 0
heap = []

# 매번 가중치가 최소인 에지를 얻기 위해 힙으로 구현한다.
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    heap.append((C, A, B))

heapify(heap)

# 에지를 힙에서 꺼내서 해당 에지의 두 노드가 같은 집합에 있는지 확인한다.
# 서로 다른 집합에 있는 경우에만 두 집합을 merge 한다.(즉 해당 에지를 MST의 에지로 추가한다.)
while count < V-1:
    C, A, B = heappop(heap)

    if find_root(A) != find_root(B):
        merge_set(A, B)
        min_weight += C
        count += 1

print(min_weight)