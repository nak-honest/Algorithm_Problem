# 걸린 시간 : 20분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

import sys
from heapq import heapify
from heapq import heappop

def find_root(node):
    while node != union_find[node]:
        node = union_find[node]

    return node

N, M = map(int, input().split())
heap = []
union_find = list(range(N+1))
depth = [0] * (N+1)

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    heap.append((C, A, B))

heapify(heap)

edges = []

while len(edges) < N - 1:
    C, A, B = heappop(heap)
    root_A = find_root(A)
    root_B = find_root(B)
    if root_A == root_B:
        continue

    edges.append(C)

    if depth[root_A] > depth[root_B]:
        union_find[root_B] = root_A
    elif depth[root_A] < depth[root_B]:
        union_find[root_A] = root_B
    else:
        depth[root_A] += 1
        union_find[root_B] = root_A

print(sum(edges) - max(edges))

