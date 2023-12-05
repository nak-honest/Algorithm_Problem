import sys
from collections import deque

N, M = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

count = 0
visited = [False] * (N + 1)
q = deque()

while True:
    start = 0
    for i in range(1, N + 1):
        if not visited[i]:
            start = i
            break

    if start == 0:
        break

    count += 1
    visited[start] = True
    q.append(start)

    while q:
        node = q.popleft()
        for next in adj_list[node]:
            if not visited[next]:
                visited[next] = True
                q.append(next)

print(count)