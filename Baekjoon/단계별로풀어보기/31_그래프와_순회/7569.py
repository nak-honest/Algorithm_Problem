# 7576 문제에서 h에 대한 부분만 추가된 것을 제외하고는 동일하다.

import sys
from collections import deque

def is_all_ripe(tomato_box):
    for h in range(len(tomato_box)):
        for i in range(len(tomato_box[h])):
            if 0 in tomato_box[h][i]:
                return False

    return True


M, N, H = map(int, input().split())
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

cur_q = deque()
next_q = deque()

for h in range(H):
    for i in range(N):
        for j in range(M):
            if box[h][i][j] == 1:
                next_q.append((h, i, j))

day = 0

while next_q:
    cur_q = next_q.copy()
    next_q.clear()

    while cur_q:
        h, i, j = cur_q.popleft()
        day = box[h][i][j]

        if i-1 >= 0 and box[h][i-1][j] == 0:
            next_q.append((h, i-1, j))
            box[h][i-1][j] = day + 1

        if i+1 < N and box[h][i+1][j] == 0:
            next_q.append((h, i+1, j))
            box[h][i+1][j] = day + 1

        if j-1 >= 0 and box[h][i][j-1] == 0:
            next_q.append((h, i, j-1))
            box[h][i][j-1] = day + 1

        if j+1 < M and box[h][i][j+1] == 0:
            next_q.append((h, i, j+1))
            box[h][i][j+1] = day + 1

        if h-1 >= 0 and box[h-1][i][j] == 0:
            next_q.append((h-1, i, j))
            box[h-1][i][j] = day + 1

        if h+1 < H and box[h+1][i][j] == 0:
            next_q.append((h+1, i, j))
            box[h+1][i][j] = day + 1

if is_all_ripe(box):
    print(day-1)
else:
    print(-1)
