# 1번 노드를 시작노드로 해서 bfs를 돌며 부모 노드 정보를 업데이트 한다.
# 루트노드를 시작으로 bfs를 돌리면, 매 노드 방문시 인접 노드중 아직 방문하지 않은 노드는 자식노드이기 떄문이다.

import sys
from collections import deque

N = int(input())
adj_list = [[] for _ in range(N+1)]
visited = [False] * (N+1)
parent = [0] * (N+1)

for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

q = deque()
visited[1] = True
q.append(1)

while q:
    node = q.popleft()

    for next in adj_list[node]:
        if not visited[next]:
            visited[next] = True
            parent[next] = node
            q.append(next)

for i in range(2, N+1):
    print(parent[i])