import sys
from collections import deque

# bfs를 돌며 각 칸이 익는데 얼마나 걸리는지를 저장한 후, 여전히 tomato_box에 0이 있다면 익지 못하는 토마토가 있음을 의미한다.
def is_all_ripe(tomato_box):
    for i in range(len(tomato_box)):
        if 0 in tomato_box[i]:
            return False

    return True


M, N = map(int, input().split())

# box에는 각 칸의 토마토가 익기 위해 필요한 최소 일수를 저장한다.
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

count = 0
cur_q = deque()
next_q = deque()

# 먼저 최초로 익은 토마토들을 큐에 넣는다.
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            next_q.append((i, j))

# bfs를 돌며 익은 토마토 주변의 토마토의 익는데 걸리는 시간을 업데이트 한다.
# next_q는 그 다음에 익는 토마토를 저장한다.
while next_q:
    cur_q = next_q.copy()
    next_q.clear()

    # cur_q에는 가장 최근에 익은 토마토들을 저장한다.
    # 따라서 cur_q 토마토의 주변 토마토를 업데이트 해야한다.
    while cur_q:
        i, j = cur_q.popleft()

        count = box[i][j]

        if i-1 >= 0 and box[i-1][j] == 0:
            box[i-1][j] = count + 1
            next_q.append((i-1, j))

        if i+1 < N and box[i+1][j] == 0:
            box[i+1][j] = count + 1
            next_q.append((i+1, j))

        if j-1 >= 0 and box[i][j-1] == 0:
            box[i][j-1] = count + 1
            next_q.append((i, j-1))

        if j + 1 < M and box[i][j+1] == 0:
            box[i][j+1] = count + 1
            next_q.append((i, j+1))

if is_all_ripe(box):
    print(count-1)
else:
    print(-1)