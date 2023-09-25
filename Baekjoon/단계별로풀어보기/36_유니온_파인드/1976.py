# 걸린 시간 : 17분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

import sys

# 유니온 파인드를 통해 전체 여행 경로가 같은 그래프에 있는지 확인한다.
def find_root(i):
    while i != union[i]:
        i = union[i]

    return i

N = int(input())
M = int(input())

adj_list = [[] for _ in range(N+1)]
for i in range(1, N+1):
    adj = list(map(int, sys.stdin.readline().split()))

    for j in range(N):
        if adj[j] == 1:
            adj_list[i].append(j+1)

plan = list(set(map(int, sys.stdin.readline().split())))

union = [i for i in range(N+1)]
depth = [0 for _ in range(N+1)]
answer = "YES"


for i in range(1, N+1):
    for adj in adj_list[i]:
        root_i = find_root(i)
        root_adj = find_root(adj)

        if root_i != root_adj:
            if depth[root_i] > depth[root_adj]:
                union[root_adj] = root_i
            elif depth[root_i] < depth[root_adj]:
                union[root_i] = root_adj
            else:
                union[root_adj] = root_i
                depth[root_adj] += 1

root = find_root(plan[0])

# 하나라도 같은 그래프에 있지 않다면 해당 도시는 갈수 없다.
for node in plan:
    if find_root(node) != root:
        answer = "NO"

print(answer)