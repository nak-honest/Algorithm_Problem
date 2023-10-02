# 걸린 시간 : 1시간 15분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

import sys
from collections import deque
from heapq import heappop, heappush

MAX_LEN = 10

def find_root(i):
    while i != union[i]:
        i = union[i]
    return i

N, M = map(int, input().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 전체 섬의 개수
island_count = 0
visited = [[False] * M for _ in range(N)]
q = deque()

# 각 섬의 경계 칸 인덱스를 저장한다.
boundary = [[]]

# 섬 정보를 업데이트한다. maps에는 해당 섬의 숫자로 업데이트하고, boundary 정보도 업데이트 한다.
for i in range(N):
    for j in range(M):
        # 새로운 섬을 발견한 경우
        if maps[i][j] == 1 and not visited[i][j]:
            q.append((i, j))
            visited[i][j] = True
            island_count += 1

            boundary.append([])

            # 인접한 모든 땅은 같은 섬이기 때문에 bfs를 돌며 해당 섬 정보를 업데이트 한다.
            while q:
                a, b = q.popleft()
                # maps에 해당 섬의 숫자로 업데이트
                maps[a][b] = island_count

                # 만약 a, b 인덱스의 땅이 경계에 위치해 있다면 boundary에 추가한다.
                if (a-1 >= 0 and maps[a-1][b] == 0) or (b-1 >= 0 and maps[a][b-1] == 0) \
                        or (a+1 < N and maps[a+1][b] == 0) or (b+1 < M and maps[a][b+1] == 0):
                    boundary[-1].append((a, b))

                # bfs를 돌며 인접한 땅이 같은 섬인지 확인한다.
                if a-1 >= 0 and maps[a-1][b] == 1 and not visited[a-1][b]:
                    q.append((a-1, b))
                    visited[a-1][b] = True
                if b-1 >= 0 and maps[a][b-1] == 1 and not visited[a][b-1]:
                    q.append((a, b-1))
                    visited[a][b-1] = True
                if a+1 < N and maps[a+1][b] == 1 and not visited[a+1][b]:
                    q.append((a+1, b))
                    visited[a+1][b] = True
                if b+1 < M and maps[a][b+1] == 1 and not visited[a][b+1]:
                    q.append((a, b+1))
                    visited[a][b+1] = True

heap = []

# 1번 섬부터 시작해서 다른 섬과의 최단 거리 정보를 업데이트 하고, 이를 heap에 추가한다.
for i in range(1, island_count):
    # i번 섬부터 다른 섬까지의 최단 거리
    min_len = [MAX_LEN] * (island_count + 1)

    # i번 섬의 경계의 칸을 하나씩 확인해서, 상하좌우 일직선으로 갔을때 다른 섬을 만나는지 확인한다.
    # 만약 다른 섬을 만난다면 해당 섬까지의 최단 거리를 업데이트한다.
    for a, b in boundary[i]:
        # 아래로 일직선으로 갔을때 다른 섬을 만나는지 확인
        cur_a = a-1
        cur_len = 0

        while cur_a >= 0 and maps[cur_a][b] != i:
            if maps[cur_a][b] != 0:
                if cur_len >= 2:
                    j = maps[cur_a][b]
                    min_len[j] = min(min_len[j], cur_len)
                break

            cur_a -= 1
            cur_len += 1

        # 왼쪽으로 일직선으로 갔을때 다른 섬을 만나는지 확인
        cur_b = b-1
        cur_len = 0

        while cur_b >= 0 and maps[a][cur_b] != i:
            if maps[a][cur_b] != 0:
                if cur_len >= 2:
                    j = maps[a][cur_b]
                    min_len[j] = min(min_len[j], cur_len)
                break

            cur_b -= 1
            cur_len += 1

        # 위로 일직선으로 갔을때 다른 섬을 만나는지 확인
        cur_a = a+1
        cur_len = 0

        while cur_a < N and maps[cur_a][b] != i:
            if maps[cur_a][b] != 0:
                if cur_len >= 2:
                    j = maps[cur_a][b]
                    min_len[j] = min(min_len[j], cur_len)
                break

            cur_a += 1
            cur_len += 1

        # 오른쪽으로 일직선으로 갔을때 다른 섬을 만나는지 확인
        cur_b = b+1
        cur_len = 0

        while cur_b < M and maps[a][cur_b] != i:
            if maps[a][cur_b] != 0:
                if cur_len >= 2:
                    j = maps[a][cur_b]
                    min_len[j] = min(min_len[j], cur_len)
                break

            cur_b += 1
            cur_len += 1

    # i번 섬의 모든 경계 칸에 대해 확인했다면 다른 섬까지의 최단 경로를 heap에 추가한다.
    for j in range(i+1, island_count+1):
        if min_len[j] != MAX_LEN:
            heappush(heap, (min_len[j], i, j))

# 크루스칼 알고리즘을 통해 MST를 구성하는 최소 비용을 구한다.
union = [i for i in range(island_count+1)]
depth = [0 for _ in range(island_count+1)]

count = 0
cost = 0

while count != island_count - 1 and heap:
    length, i, j = heappop(heap)

    root_i = find_root(i)
    root_j = find_root(j)

    if root_i == root_j:
        continue

    count += 1
    cost += length

    if depth[root_i] > depth[root_j]:
        union[root_j] = root_i
    elif depth[root_i] < depth[root_j]:
        union[root_i] = root_j
    else:
        union[root_j] = root_i
        depth[root_i] += 1

if count == island_count - 1:
    print(cost)
else:
    print(-1)