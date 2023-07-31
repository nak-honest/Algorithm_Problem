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
    adj_list[i].sort(reverse=True)

visited[R] = True
count = 0
q.append(R)

while q:
    node = q.popleft()
    count += 1
    visit_order[node-1] = count

    for next in adj_list[node]:
        if not visited[next]:
            visited[next] = True
            q.append(next)

print(*visit_order, sep='\n')