# 걸린 시간 : 10분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

import sys

def find_root(i):
    while i != union[i]:
        i = union[i]

    return i

n, m = map(int, input().split())

union = [i for i in range(n)]
depth = [0 for _ in range(n)]

order = 0

# 두 노드를 잇는 간선을 하나씩 입력받는데, 만약 두 노드가 이미 같은 union find에 포함되어 있다면 그때 사이클이 생기는 것이다.
for i in range(1, m+1):
    if order != 0:
        continue

    u, v = map(int, sys.stdin.readline().split())
    root_u = find_root(u)
    root_v = find_root(v)

    if root_u == root_v:
        order = i

    else:
        if depth[root_u] > depth[root_v]:
            union[root_v] = root_u
        elif depth[root_u] < depth[root_v]:
            union[root_u] = root_v
        else:
            union[root_v] = root_u
            depth[root_u] += 1

print(order)
