# 걸린 시간 : 13분
# 제출 횟수 : 2번
# 풀이 참조 : x
# 반례 참조 : x

import sys
from heapq import heappop, heappush

def find_root(i, union):
    while i != union[i]:
        i = union[i]

    return i

# 테스트 케이스가 여러개이다. 문제를 잘 읽자!
while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break

    road = []

    total_cost = 0

    for _ in range(n):
        x, y, z = map(int, sys.stdin.readline().split())
        heappush(road, (z, x, y))
        total_cost += z

    union_find = [i for i in range(m)]
    depth = [0 for _ in range(m)]

    count = 0
    cost = 0

    # 크루스칼 알고리즘을 이용해 최소 MST의 비용을 찾는다.
    while count != m-1:
        z, x, y = heappop(road)

        root_x = find_root(x, union_find)
        root_y = find_root(y, union_find)

        if root_x == root_y:
            continue

        count += 1
        cost += z

        if depth[root_x] > depth[root_y]:
            union_find[root_y] = root_x
        elif depth[root_x] < depth[root_y]:
            union_find[root_x] = root_y
        else:
            union_find[root_y] = root_x
            depth[root_x] += 1
    
    print(total_cost - cost)
