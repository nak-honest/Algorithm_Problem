# N이 K보다 크다면 2를 곱할 필요가 없다.
# 즉 N < K 일때에만 2를 곱하면 된다는 것이다.
# 따라서 MAX_SIZE는 K가 100000일때를 기준으로 하여 200000으로 잡는다.
MAX_SIZE = 200000

from collections import deque

N, K = map(int, input().split())

q = deque()
visited = [False] * MAX_SIZE

prev_nodes = [-1] * MAX_SIZE

q.append((N, 0, -1))
visited[N] = True

# bfs를 돌며 각 노드에 도달하는데 걸리는 시간, 그리고 이전 노드 정보를 업데이트한다.
while q:
    node, cnt, prev = q.popleft()
    prev_nodes[node] = prev

    if node == K:
        print(cnt)
        break

    if node-1 >= 0 and not visited[node-1]:
        q.append((node-1, cnt+1, node))
        visited[node-1] = True

    if node+1 <= K and not visited[node+1]:
        q.append((node+1, cnt+1, node))
        visited[node+1] = True

    if node < K and not visited[node*2]:
        q.append((node*2, cnt+1, node))
        visited[node*2] = True

# prev_nodes를 기반으로 이동해야 하는 경로를 추적한다.
cur = K
answer = deque()

while cur != -1:
    answer.appendleft(cur)
    cur = prev_nodes[cur]

print(*answer)
