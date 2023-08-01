import sys
from collections import deque

N, M, V = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

for i in range(1, N+1):
    adj_list[i].sort()



# dfs
dq = deque()
dq.append(V)

while dq:
    node = dq.pop()
    if not visited[node]:
        print(node, end=' ')
        visited[node] = True

    for next_node in reversed(adj_list[node]):
        if not visited[next_node]:
            dq.append(next_node)

print()


# bfs
visited = [False] * (N+1)

dq.append(V)
visited[V] = True

while dq:
    node = dq.popleft()

    print(node, end=' ')

    for next_node in adj_list[node]:
        if not visited[next_node]:
            dq.append(next_node)
            visited[next_node] = True
