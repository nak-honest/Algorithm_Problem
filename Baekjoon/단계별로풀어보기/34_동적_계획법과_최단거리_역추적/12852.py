from collections import deque

N = int(input())

q = deque()
visited = [False] * (N+1)
prev = [-1] * (N+1)

q.append((N, 0))
visited[N] = True

# bfs를 돌며 각 숫자에 도달하는데 필요한 최소 count를 계산한다.
while q:
    X, count = q.popleft()

    if X == 1:
        print(count)
        break

    # 다음 노드를 queue에 집어넣는다. 이때 최단 거리를 역추적 하기 위해 이전 노드 정보도 업데이트 한다.
    if X % 3 == 0 and not visited[X//3]:
        q.append((X//3, count+1))
        visited[X//3] = True
        prev[X//3] = X

    if X % 2 == 0 and not visited[X//2]:
        q.append((X//2, count+1))
        visited[X//2] = True
        prev[X//2] = X

    if not visited[X-1]:
        q.append((X-1, count+1))
        visited[X-1] = True
        prev[X-1] = X

answer = deque()
answer.appendleft(1)

# 최단거리를 역추적한다.
cur = 1
while cur != N:
    prev_node = prev[cur]
    answer.appendleft(prev_node)
    cur = prev_node

print(*answer)
