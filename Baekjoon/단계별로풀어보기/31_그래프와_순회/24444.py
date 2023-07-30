import sys
from collections import deque

N, M, R = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
q = deque()
visited = [False] * (N+1)
visit_order = [0] * N

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

for i in range(1, N+1):
    adj_list[i].sort()

q.append(R)
visited[R] = True
count = 0

while q:
    node = q.popleft()
    count += 1
    visit_order[node-1] = count

    for next in adj_list[node]:
        if not visited[next]:
            q.append(next)
            visited[next] = True

print(*visit_order, sep='\n')