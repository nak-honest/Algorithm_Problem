# 걸린 시간 : 30분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

from itertools import combinations
from collections import deque

N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]


blanks = []
virus = []

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            blanks.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

answer = 0

for new_walls in combinations(blanks, 3):
    safe_count = len(blanks) - 3
    visited = [[False] * M for _ in range(N)]
    q = deque(virus)

    for i, j in virus:
        visited[i][j] = True

    # 실제로는 새로 세우는 벽이지만, 방문한 것으로 쳐서 더이상 방문하지 못하도록 만든다.
    for i, j in new_walls:
        visited[i][j] = True

    while q:
        i, j = q.popleft()

        if i+1 < N and not visited[i+1][j] and lab[i+1][j] == 0:
            visited[i+1][j] = True
            safe_count -= 1
            q.append((i+1, j))

        if j+1 < M and not visited[i][j+1] and lab[i][j+1] == 0:
            visited[i][j+1] = True
            safe_count -= 1
            q.append((i, j+1))

        if i-1 >= 0 and not visited[i-1][j] and lab[i-1][j] == 0:
            visited[i-1][j] = True
            safe_count -= 1
            q.append((i-1, j))

        if j-1 >= 0 and not visited[i][j-1] and lab[i][j-1] == 0:
            visited[i][j-1] = True
            safe_count -= 1
            q.append((i, j-1))


    answer = max(answer, safe_count)

print(answer)
