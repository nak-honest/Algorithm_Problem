import sys
from heapq import heappop, heappush
from collections import deque


N = int(input())

apart_map = [list(sys.stdin.readline().rstrip('\n')) for _ in range(N)]
heap = []

# bfs를 돌며 start와 인접해 있는 아파트의 개수를 구해서 반환한다.
# 또한 해당 아파트가 어느 단지에 속했는지 이제 알게되었으므로 0으로 바꾼다.
def bfs(start):
    count = 0
    q = deque()
    q.append(start)
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True

    while q:
        i, j = q.popleft()
        count += 1
        apart_map[i][j] = '0'

        if i - 1 >= 0 and not visited[i - 1][j] and apart_map[i - 1][j] == '1':
            visited[i - 1][j] = True
            q.append((i - 1, j))
        if i + 1 < N and not visited[i + 1][j] and apart_map[i + 1][j] == '1':
            visited[i + 1][j] = True
            q.append((i + 1, j))
        if j - 1 >= 0 and not visited[i][j - 1] and apart_map[i][j - 1] == '1':
            visited[i][j - 1] = True
            q.append((i, j - 1))
        if j + 1 < N and not visited[i][j + 1] and apart_map[i][j + 1] == '1':
            visited[i][j + 1] = True
            q.append((i, j + 1))

    return count

# i, j가 아파트라면 해당 아파트와 인접해있는 아파트의 개수를 구해서 min heap에 넣는다.
for i in range(N):
    for j in range(N):
        if apart_map[i][j] == '1':
            heappush(heap, bfs((i, j)))

# 단지의 개수 출력
print(len(heap))

# 오름차순으로 단지별 아파트 개수 출력
while heap:
    print(heappop(heap))
