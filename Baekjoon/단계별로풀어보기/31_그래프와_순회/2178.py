import sys
from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, list(sys.stdin.readline().rstrip('\n')))) for _ in range(N)]

# bfs를 위한 큐로 방문할 칸을 저장한다.
queue = deque()
# 해당 칸을 방문했는지 여부를 저장한다.
visited = [[False] * M for _ in range(N)]
# 각 칸까지 이동하는데 필요한 칸의 개수를 저장한다.
count = [[1] * M for _ in range(N)]

# 처음에 (0, 0)을 시작점으로 하기 때문에 큐에 넣는다.
queue.append((0, 0))
visited[0][0] = True

# bfs를 하다 도착점을 가장 먼저 발견한 경우가 최단 거리이다.
# 그 이유는 인접한 노드로 퍼지면서 도착점으로 가는 여러 경로를 번갈아가면서 확인하기 떄문이다.
# 즉 depth가 깊어지는 순이 아니라 같은 depth의 노드를 다 방문한 다음에 다음 depth를 방문하는데,
# depth가 해당 노드까지 가는데 필요한 칸의 개수이기 때이다. -> 도착점을 가장 먼저 발견한 경로가 가장 depth가 낮은 것이기 떄문!
while deque:
    i, j = queue.popleft()

    # 방문한 노드가 도착점이라면 count를 방문하고 bfs를 멈춘다.
    if i == N-1 and j == M-1:
        print(count[i][j])
        break

    # 상하좌우 한칸씩 이동 가능한지 보고, 이동 가능하다면 해당 칸을 큐에 넣는다.
    # 여기서 이동 가능은 해당 칸이 1이고, 미로를 벗어나는 인덱스가 아니며, 아직 방문하지 않은 노드임을 의미한다.

    # 밑의 칸이 방문 가능하다면 밑의 칸을 큐에 넣는다.
    if i + 1 < N and maze[i+1][j] == 1 and not visited[i+1][j]:
        queue.append((i+1, j))
        visited[i+1][j] = True
        count[i+1][j] = count[i][j] + 1

    # 위의 칸이 방문 가능하다면 위의 칸을 큐에 넣는다.
    if i > 0 and maze[i-1][j] == 1 and not visited[i-1][j]:
        queue.append((i-1, j))
        visited[i-1][j] = True
        count[i-1][j] = count[i][j] + 1

    # 오른쪽 칸이 방문 가능하다면 오른쪽 칸을 큐에 넣는다.
    if j + 1 < M and maze[i][j+1] == 1 and not visited[i][j+1]:
        queue.append((i, j+1))
        visited[i][j+1] = True
        count[i][j+1] = count[i][j] + 1

    # 왼쪽 칸이 방문 가능하다면 왼쪽 칸을 큐에 넣는다.
    if j > 0 and maze[i][j-1] == 1 and not visited[i][j-1]:
        queue.append((i, j-1))
        visited[i][j-1] = True
        count[i][j-1] = count[i][j] + 1