import sys
from collections import deque

n, m = map(int, input().split())

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            answer[i][j] = 0

start = (0, 0)
for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            start = (i, j)
            break

# bfs를 돌며 거리를 업데이트 한다.
visited = [[False] * m for _ in range(n)]
q = deque()

q.append(start)
visited[start[0]][start[1]] = True
answer[start[0]][start[1]] = 0

while q:
    i, j = q.popleft()
    count = answer[i][j]

    # 위로 이동할 수 있고, 아직 방문하지 않은 경우
    if i - 1 >= 0 and not visited[i - 1][j] and maps[i - 1][j] == 1:
        visited[i - 1][j] = True
        answer[i - 1][j] = count + 1
        q.append((i - 1, j))

    # 왼쪽으로 이동할 수 있고, 아직 방문하지 않은 경우
    if j - 1 >= 0 and not visited[i][j - 1] and maps[i][j - 1] == 1:
        visited[i][j - 1] = True
        answer[i][j - 1] = count + 1
        q.append((i, j - 1))

    # 밑으로 이동할 수 있고, 아직 방문하지 않은 경우
    if i + 1 < n and not visited[i + 1][j] and maps[i + 1][j] == 1:
        visited[i + 1][j] = True
        answer[i + 1][j] = count + 1
        q.append((i + 1, j))

    # 오른쪽으로 이동할 수 있고, 아직 방문하지 않은 경우
    if j + 1 < m and not visited[i][j + 1] and maps[i][j + 1] == 1:
        visited[i][j + 1] = True
        answer[i][j + 1] = count + 1
        q.append((i, j + 1))

for i in range(n):
    print(*answer[i])
