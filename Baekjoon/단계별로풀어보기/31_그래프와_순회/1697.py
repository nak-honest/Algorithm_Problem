from collections import deque

MAX_LEN = 100_001

N, K = map(int, input().split())

q = deque()
visited = [False] * MAX_LEN

visited[N] = True
q.append((N, 0))

# bfs를 돌며 각 점에 방문하는데 필요한 최소 시간을 구한다.
while q:
    node, count = q.popleft()
    if node == K:
        print(count)
        break

    if node - 1 >= 0 and not visited[node-1]:
        visited[node-1] = True
        q.append((node-1, count+1))

    if node + 1 < MAX_LEN and not visited[node+1]:
        visited[node+1] = True
        q.append((node+1, count+1))

    if node * 2 < MAX_LEN and not visited[node*2]:
        visited[node*2] = True
        q.append((node*2, count+1))
