import sys
from collections import deque


N, M = map(int, input().split())
mat = [list(map(int, list(sys.stdin.readline().rstrip('\n')))) for _ in range(N)]

# q에는 (인덱스, 최단 거리, 벽 부셨는지 여부) 를 저장한다.
q = deque()

# visited는 벽을 부수지 않고 해당 칸을 방문했는지 여부를 저장한다.
visited = [[False] * M for _ in range(N)]

# visited_break는 벽을 부수고 해당 칸을 방문했는지 여부를 저장한다.
# 이때 visited가 먼저 true가 된 경우(즉 벽을 부수고 해당 칸에 먼저 도달한 경우)에는 방문하지 않는다.
visited_break = [[False] * M for _ in range(N)]

q.append(((0, 0), 1, False))
visited[0][0] = True

answer = -1

# bfs를 돌며 각 칸에 도달할 수 있는 count를 업데이트 한다.
while q:
    index, count, is_break = q.popleft()
    i, j = index

    if i == N-1 and j == M-1:
        answer = count
        break

    # 해당 칸까지 벽을 한번도 부수지 않고 방문했던 경우에는 방문하지 않는다.
    # 만약 visited_break[i-1][j]는 False 여도 방문할 필요가 없다.
    # 해당 칸까지 도달하는데 벽을 부순 경로는 벽을 부수지 않고 도달한 경로보다 항상 같거나 느리기 때문이다.
    if i-1 >= 0 and not visited[i-1][j]:
        # 만약 해당 칸까지 도달하는데 아직 벽을 부수지 않았다면 visited를 업데이트 한다.
        # 이때 visited_break가 먼저 True가 되었더라도 방문한다.
        # 벽을 부수지 않고 간 경로가 현재는 더 길더라도, 이후에 다른 벽을 부셔서 가는 경로가 더 짧을 수 있기 때문이다.
        # 즉 벽을 부수지 않고 도달한 경로는 벽을 부술수 있는 기회가 있기 때문에 이후에 경로가 더 짧아질 수 있다.
        if mat[i-1][j] == 0 and not is_break:
            q.append(((i-1, j), count+1, is_break))
            visited[i-1][j] = True

        # 만약 해당 칸까지 도달하는데 벽을 부순적이 있고, 벽을 부셔서 해당 칸까지 도달한 게 처음이라면 visited_break를 업데이트 한다.
        elif mat[i-1][j] == 0 and is_break and not visited_break[i-1][j]:
            q.append(((i-1, j), count+1, is_break))
            visited_break[i-1][j] = True

        # 만약 아직 벽을 부수지 않았는데 해당 칸이 벽이라면 벽을 부셔서 해당 칸으로 간다.
        elif mat[i-1][j] == 1 and not is_break:
            q.append(((i-1, j), count+1, True))

    # 나머지 인접한 칸에 대해서도 똑같이 적용한다.
    if i+1 < N and not visited[i+1][j]:
        if mat[i+1][j] == 0 and not is_break:
            q.append(((i+1, j), count+1, is_break))
            visited[i+1][j] = True
        elif mat[i+1][j] == 0 and is_break and not visited_break[i+1][j]:
            q.append(((i+1, j), count+1, is_break))
            visited_break[i+1][j] = True
        elif mat[i+1][j] == 1 and not is_break:
            q.append(((i+1, j), count+1, True))

    if j-1 >= 0 and not visited[i][j-1]:
        if mat[i][j-1] == 0 and not is_break:
            q.append(((i, j-1), count+1, is_break))
            visited[i][j-1] = True
        elif mat[i][j-1] == 0 and is_break and not visited_break[i][j-1]:
            q.append(((i, j-1), count+1, is_break))
            visited_break[i][j-1] = True
        elif mat[i][j-1] == 1 and not is_break:
            q.append(((i, j-1), count+1, True))

    if j+1 < M and not visited[i][j+1]:
        if mat[i][j+1] == 0 and not is_break:
            q.append(((i, j+1), count+1, is_break))
            visited[i][j+1] = True
        elif mat[i][j+1] == 0 and is_break and not visited_break[i][j+1]:
            q.append(((i, j+1), count+1, is_break))
            visited_break[i][j+1] = True
        elif mat[i][j+1] == 1 and not is_break:
            q.append(((i, j+1), count+1, True))

print(answer)
