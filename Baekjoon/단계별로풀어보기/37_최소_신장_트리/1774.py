# 걸린 시간 : 24분
# 제출 횟수 : 2번
# 풀이 참조 : x
# 반례 참조 : x

import sys
from heapq import heappop, heappush

def get_length(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def find_root(i):
    while i != union[i]:
        i = union[i]

    return i

N, M = map(int, input().split())

nodes = []
for _ in range(N):
    X, Y = map(int, sys.stdin.readline().split())
    nodes.append((X, Y))

union = [i for i in range(N)]
depth = [0 for _ in range(N)]

# 이미 연결된 간선들을 set에 저장한다.
prev_adj = set()
count = 0

# 이미 연결된 간선들을 업데이트한다.
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    i -= 1
    j -= 1

    prev_adj.add((i, j))
    prev_adj.add((j, i))

    root_i = find_root(i)
    root_j = find_root(j)

    if root_i != root_j:
        count += 1

        if depth[root_i] > depth[root_j]:
            union[root_j] = root_i
        elif depth[root_i] < depth[root_j]:
            union[root_i] = root_j
        else:
            union[root_j] = root_i
            depth[root_i] += 1

heap = []

# 모든 연결 가능한 간선들 중 prev_adj에 없는 간선만 heap에 추가한다.
for i in range(N):
    for j in range(i+1, N):
        if (i, j) in prev_adj:
            continue

        length = get_length(nodes[i], nodes[j])
        heappush(heap, (length, i, j))

cost = 0

# heap에서 비용이 가장 작은 간선을 하나씩 빼서 추가한다.
while count < N-1:
    length, i, j = heappop(heap)

    root_i = find_root(i)
    root_j = find_root(j)

    # 이미 같은 union find에 있다면 두 노드는 연결되어 있다는 것이다.
    if root_i == root_j:
        continue

    count += 1
    cost += length

    if depth[root_i] > depth[root_j]:
        union[root_j] = root_i
    elif depth[root_i] < depth[root_j]:
        union[root_i] = root_j
    else:
        union[root_j] = root_i
        depth[root_i] += 1

# round 함수를 사용하면 4.00 이 아니라 4.0 으로 출력된다.
# 따라서 포맷팅을 사용해서 출력한다.
print(f'{cost:.2f}')
