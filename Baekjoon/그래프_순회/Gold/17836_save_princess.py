import sys
from collections import deque


N, M, T = map(int, input().split())
castle = [list(map(int, list(sys.stdin.readline().split()))) for _ in range(N)]


def bfs(dest):
    queue = deque()
    visited = [[False] * M for _ in range(N)]
    count = [[0] * M for _ in range(N)]

    queue.append((0, 0))
    visited[0][0] = True

    while queue:
        i, j = queue.popleft()

        # 방문한 노드가 도착점이라면 count를 방문하고 bfs를 멈춘다.
        if i == dest[0] and j == dest[1]:
            return count[i][j]

        # 상하좌우 한칸씩 이동 가능한지 보고, 이동 가능하다면 해당 칸을 큐에 넣는다.
        # 여기서 이동 가능은 해당 칸이 1이고, 미로를 벗어나는 인덱스가 아니며, 아직 방문하지 않은 노드임을 의미한다.

        # 밑의 칸이 방문 가능하다면 밑의 칸을 큐에 넣는다.
        if i + 1 < N and castle[i + 1][j] != 1 and not visited[i + 1][j]:
            queue.append((i + 1, j))
            visited[i + 1][j] = True
            count[i + 1][j] = count[i][j] + 1

        # 위의 칸이 방문 가능하다면 위의 칸을 큐에 넣는다.
        if i > 0 and castle[i - 1][j] != 1 and not visited[i - 1][j]:
            queue.append((i - 1, j))
            visited[i - 1][j] = True
            count[i - 1][j] = count[i][j] + 1

        # 오른쪽 칸이 방문 가능하다면 오른쪽 칸을 큐에 넣는다.
        if j + 1 < M and castle[i][j + 1] != 1 and not visited[i][j + 1]:
            queue.append((i, j + 1))
            visited[i][j + 1] = True
            count[i][j + 1] = count[i][j] + 1

        # 왼쪽 칸이 방문 가능하다면 왼쪽 칸을 큐에 넣는다.
        if j > 0 and castle[i][j - 1] != 1 and not visited[i][j - 1]:
            queue.append((i, j - 1))
            visited[i][j - 1] = True
            count[i][j - 1] = count[i][j] + 1

    return -1


without_gram = bfs((N-1, M-1))
with_gram = -1

for i in range(N):
    for j in range(M):
        if castle[i][j] == 2:
            with_gram = bfs((i, j))

            if with_gram != -1:
                with_gram += N - 1 - i + M - 1 - j

if (without_gram != -1 and with_gram != -1) and min(without_gram, with_gram) <= T:
    print(min(without_gram, with_gram))
elif without_gram != -1 and without_gram <= T:
    print(without_gram)
elif with_gram != -1 and with_gram <= T:
    print(with_gram)
else:
    print("Fail")