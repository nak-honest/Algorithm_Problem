# 걸린 시간 : 30분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

'''
부모, 자식이 전부 얼리 어댑터라면 자신은 얼리 어댑터가 안되면 된다.
자신이 얼리 어댑터가 아니라면 부모, 자식은 모두 얼리 어댑터이어야 한다.
밑의 depth부터 위로 올라가면서, 자신이 얼리어댑터인 경우, 아닌 경우의 최소 얼리어댑터 수를 dp에 저장한다.
자신이 얼리어댑터인 경우 = 각 자식의 최소의 경우를 모두 더한뒤 + 1을 한다.
자신이 얼리어댑터가 아닌 경우 = 모든 자식이 얼리어댑터인 경우를 모두 더한다.
'''

import sys
from collections import deque

N = int(input())
adj_list = [[] for _ in range(N+1)]
parent = [-1] * (N+1)
children = [[] for _ in range(N+1)]
depth = [-1] * (N+1)

root = 1
q = deque()
q.append(root)
depth[root] = 0

for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

while q:
    p = q.popleft()
    for c in adj_list[p]:
        if c != parent[p]:
            parent[c] = p
            children[p].append(c)
            depth[c] = depth[p] + 1
            q.append(c)

# 같은 depth의 노드를 모아 둔다.
same_depth_nodes = [[] for _ in range(max(depth)+1)]
for i in range(1, N+1):
    same_depth_nodes[depth[i]].append(i)

# dp[0][i]는 노드 i가 얼리 어댑터인 경우이고, dp[1][i]는 노드 i가 얼리 어댑터가 아닌 경우이다.
dp = [[0] * (N+1) for _ in range(2)]

# 가장 깊은 depth의 노드부터 위로 올라가면서 dp 값을 계산한다.
for nodes in reversed(same_depth_nodes):
    for node in nodes:
        # node가 얼리 어댑터인 경우이므로 1을 먼저 더한다.
        dp[0][node] = 1
        # 자식들의 dp 값을 더한다.
        for child in children[node]:
            # 각 자식의 최소 dp 값을 더한다. node가 얼리 어댑터 이므로 자식은 얼리 어댑터이든, 아니든 상관 없다.
            dp[0][node] += min(dp[0][child], dp[1][child])
            # node가 얼리어댑터가 아니므로 모든 자식이 얼리어댑터이어야 한다. 각 자식이 얼리어댑터인 경우의 dp값을 더한다.
            dp[1][node] += dp[0][child]

print(min(dp[0][1], dp[1][1]))

