# count % 10을 graph에 직접 저장하다보니 0으로 저장되어 계속 틀렸음.

# 걸린 시간 : 30분
# 제출 횟수 : 4번
# 풀이 참조 : x
# 반례 참조 : x

'''
먼저 각 빈칸(0)이 갈 수 있는 칸을 센다.
-> 서로 연결되어 있는 빈칸은 전부 갈수 있는 칸의 개수가 같다!! 즉 bfs 몇번만 돌리면 됨.
-> 그리고 이 bfs로 연결되어 있는 영역을 숫자로 표시한다.

그 후 각 벽이 갈수 있는 칸을 세는데, 다음과 같은 방식으로 센다.
-> 상하좌우 인접한 칸 중 빈칸인 칸에 대해서만 갈 수 있는 칸의 개수를 더한다. 이때 빈칸의 영역은 서로 달라야한다.
-> 상하좌우 인접한 칸 중 같은 영역의 빈칸은 하나만 선택해서 더한다.
-> 그 더한 값에 자기 자신을 포함해 1을 더한 값이 해당 위치에서 이동할 수 있는 칸이 된다
'''

import sys
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, list(sys.stdin.readline().rstrip('\n')))) for _ in range(N)]
area = 0
area_of_empty_space = dict()
count_of_area = []

visited = [[False] * M for _ in range(N)]
udlr = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and not visited[i][j]:
            count = 0
            q = deque()
            q.append((i, j))
            visited[i][j] = True

            while q:
                node_i, node_j = q.popleft()
                count += 1
                area_of_empty_space[(node_i, node_j)] = area

                for add_i, add_j in udlr:
                    if 0 <= node_i + add_i < N and 0 <= node_j + add_j < M \
                            and graph[node_i+add_i][node_j+add_j] == 0 and not visited[node_i+add_i][node_j+add_j]:
                        visited[node_i+add_i][node_j+add_j] = True
                        q.append((node_i+add_i, node_j+add_j))

            count_of_area.append(count)
            area += 1

answer = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            count = 1
            areas = set()
            for add_i, add_j in udlr:
                if 0 <= i + add_i < N and 0 <= j + add_j < M and graph[i+add_i][j+add_j] == 0:
                    areas.add(area_of_empty_space[(i+add_i, j+add_j)])

            for area in areas:
                count += count_of_area[area]

            answer[i][j] = count % 10

for i in range(N):
    print(*answer[i], sep='')
