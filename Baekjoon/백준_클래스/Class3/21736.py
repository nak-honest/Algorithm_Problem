import sys
from collections import deque

N, M = map(int, input().split())
campus = [list(sys.stdin.readline().rstrip('\n')) for _ in range(N)]

start = (0, 0)

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            start = (i, j)
            break
    if start != (0, 0):
        break

q = deque()
visited = [[False] * M for _ in range(N)]
q.append(start)
visited[start[0]][start[1]] = True
count = 0

while q:
    i, j = q.popleft()

    if campus[i][j] == 'P':
        count += 1

    if i - 1 >= 0 and not visited[i-1][j] and campus[i-1][j] != 'X':
        q.append((i-1, j))
        visited[i-1][j] = True

    if j - 1 >= 0 and not visited[i][j-1] and campus[i][j-1] != 'X':
        q.append((i, j-1))
        visited[i][j-1] = True

    if i + 1 < N and not visited[i+1][j] and campus[i+1][j] != 'X':
        q.append((i+1, j))
        visited[i+1][j] = True

    if j + 1 < M and not visited[i][j+1] and campus[i][j+1] != 'X':
        q.append((i, j+1))
        visited[i][j+1] = True

if count == 0:
    print("TT")
else:
    print(count)
