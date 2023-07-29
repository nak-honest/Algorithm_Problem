import sys

N, M, R = map(int, input().split())

adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

for i in range(1, N+1):
    adj_list[i].sort()

visit_order = [0] * N

visited = [False] * (N+1)
stack = [R]

count = 0

while stack:
    node = stack.pop()
    if not visited[node]:
        visited[node] = True
        count += 1
        visit_order[node-1] = count

        for next in adj_list[node]:
            if not visited[next]:
                stack.append(next)

print(*visit_order, sep='\n')
