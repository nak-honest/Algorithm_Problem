# 걸린 시간 : 20분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

import sys
from collections import deque

N = int(input())
people_count = [0] + list(map(int, sys.stdin.readline().split()))

root = 1
adj_list = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

parent = [-1] * (N+1)
children = [[] for _ in range(N+1)]
q = deque()
q.append((root, 0))

# same_depth[i]에는 depth가 i인 노드들을 모아 놓는다.
same_depth = [[root]]

while q:
    p, d = q.popleft()

    for c in adj_list[p]:
        if parent[p] == c:
            continue
        parent[c] = p
        children[p].append(c)
        q.append((c, d+1))

        if len(same_depth) == d+1:
            same_depth.append([])

        same_depth[d+1].append(c)

# dp[i]는 노드 i를 루트노드로 하는 서브 트리에서 우수 마을 인구 수의 최대 합을 의미한다.
# 각 노드의 dp 값은 max(자식들의 dp 합, 자신의 인구 수 + 자식의 자식들의 dp 합)이다.
# 이 dp 값을 가장 depth가 낮은 노드들부터 계산하면서 위로 올라간다.
dp = [0] * (N+1)

for nodes in reversed(same_depth):
    for parent in nodes:
        children_dp_sum = 0
        grand_children_dp_sum = 0

        for child in children[parent]:
            children_dp_sum += dp[child]
            for grand_child in children[child]:
                grand_children_dp_sum += dp[grand_child]

        dp[parent] = max(children_dp_sum, grand_children_dp_sum + people_count[parent])

print(dp[root])
