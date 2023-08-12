import sys
from collections import deque

# bfs를 돌며 인접해 있는 1을 전부 2로 바꾸어 준다.
def bfs(graph, start, N, M):
    _i, _j = start
    q = deque()
    visited = [[False] * M for _ in range(N)]

    q.append((_i, _j))
    visited[_i][_j] = True

    while q:
        i, j = q.popleft()
        graph[i][j] = 2

        if i - 1 >= 0 and not visited[i-1][j] and graph[i-1][j] == 1:
            q.append((i-1, j))
            visited[i-1][j] = True

        if i + 1 < N and not visited[i+1][j] and graph[i+1][j] == 1:
            q.append((i+1, j))
            visited[i+1][j] = True

        if j - 1 >= 0 and not visited[i][j-1] and graph[i][j-1] == 1:
            q.append((i, j-1))
            visited[i][j-1] = True

        if j + 1 < M and not visited[i][j+1] and graph[i][j+1] == 1:
            q.append((i, j+1))
            visited[i][j+1] = True


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    count = 0

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        field[Y][X] = 1

    # 배추밭의 모든 인덱스를 하나씩 다 탐색하면서 1이라면 해당 1 주변의 모든 배추를 찾기 위해 bfs를 돌린다.
    # 이때 bfs를 돌면서 2로 바꿔주어 해당 셀의 배추에 방문했음을 표시해준다.
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                bfs(field, (i, j), N, M)
                count += 1

    print(count)