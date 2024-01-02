# 처음에 아기 상어의 위치를 확인 했으면 0으로 초기화 해야 하는데, 계속 9로 두고 풀려고 했다.
# 문제 자체는 그렇게 어렵지 않았음!!

# 걸린 시간 : 1시간
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

import sys
from collections import deque

N = int(input())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cur_size = 2
eat_count = 0

shark_position = (0, 0)
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            shark_position = (i, j)
            sea[i][j] = 0

old_shark_position = (-1, -1)
total_count = 0

# 상어가 더이상 먹을 물고기가 없을 때까지 반복한다.
while old_shark_position != shark_position:
    old_shark_position = shark_position
    q = deque()
    q.append((shark_position, 0))
    visited = [[False] * N for _ in range(N)]
    visited[shark_position[0]][shark_position[1]] = True

    # min_count는 상어가 다음 물고기를 먹는데 필요한 최소 이동 거리이다.
    min_count = sys.maxsize

    while q:
        position, count = q.popleft()
        i, j = position

        if count == min_count:
            if sea[i][j] != 0 and sea[i][j] < cur_size:
                # sea[i][j]에 있는 물고기가 먹을 수 있는 물고기인데, 아직 shark_position이 업데이트 안된 경우
                if old_shark_position == shark_position:
                    shark_position = (i, j)
                    total_count += count

                # sea[i][j]에 있는 물고기를 먹을 수 있고, 이전의 shark_position보다 더 위, 왼쪽에 있는 경우
                if i < shark_position[0] or (i == shark_position[0] and j < shark_position[1]):
                    shark_position = (i, j)
            continue

        if i - 1 >= 0 and not visited[i-1][j] and sea[i-1][j] <= cur_size:
            q.append(((i-1, j), count + 1))
            visited[i-1][j] = True
            if sea[i-1][j] < cur_size and sea[i-1][j] != 0:
                min_count = count + 1

        if j - 1 >= 0 and not visited[i][j-1] and sea[i][j-1] <= cur_size:
            q.append(((i, j-1), count + 1))
            visited[i][j-1] = True
            if sea[i][j-1] < cur_size and sea[i][j-1] != 0:
                min_count = count + 1

        if i + 1 < N and not visited[i+1][j] and sea[i+1][j] <= cur_size:
            q.append(((i+1, j), count + 1))
            visited[i+1][j] = True
            if sea[i+1][j] < cur_size and sea[i+1][j] != 0:
                min_count = count + 1

        if j + 1 < N and not visited[i][j+1] and sea[i][j+1] <= cur_size:
            q.append(((i, j+1), count + 1))
            visited[i][j+1] = True
            if sea[i][j+1] < cur_size and sea[i][j+1] != 0:
                min_count = count + 1

    # 다음에 먹을 물고기가 있는 경우 먹는다.
    if old_shark_position != shark_position:
        sea[shark_position[0]][shark_position[1]] = 0
        eat_count += 1
        if eat_count == cur_size:
            cur_size += 1
            eat_count = 0

print(total_count)