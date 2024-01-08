# 걸린 시간 : 50분
# 제출 횟수 : 2번
# 풀이 참조 : x
# 반례 참조 : x

'''
일단 가장 외부 빈 공간이 외부 공기로 취급된다.
-> 각 칸에 번호를 부여한다.

일단 외부 공기는 -1으로 한다.
치즈는 1로 한다.
내부 공기는 0으로 한다.

내부 공기는 외부 공기에서 bfs를 돌릴때 방문되지 않는 0인 칸이다!
그리고 한번 외부 공기가 되면 계속 외부 공기로 유지되기 때문에 이미 방문한 노드로 취급한다.
'''

import sys
from collections import deque

N, M = map(int, input().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
q = deque()

q.append((0, 0))
visited[0][0] = True

# 먼저 처음에 bfs를 돌며 외부 공기를 찾는다. (0, 0)은 항상 외부 공기임!
while q:
    i, j = q.popleft()
    paper[i][j] = -1

    if i-1 >= 0 and not visited[i-1][j] and paper[i-1][j] == 0:
        q.append((i-1, j))
        visited[i-1][j] = True

    if j-1 >= 0 and not visited[i][j-1] and paper[i][j-1] == 0:
        q.append((i, j-1))
        visited[i][j-1] = True

    if i+1 < N and not visited[i+1][j] and paper[i+1][j] == 0:
        q.append((i+1, j))
        visited[i+1][j] = True

    if j+1 < M and not visited[i][j+1] and paper[i][j+1] == 0:
        q.append((i, j+1))
        visited[i][j+1] = True

answer = 0
remain = set()
inner = set()

# remain은 남은 치즈의 인덱스, inner는 내부 공기의 인덱스를 저장한다.
for i in range(N):
    for j in range(M):
        if paper[i][j] == 1:
            remain.add((i, j))
        elif paper[i][j] == 0:
            inner.add((i, j))

# 남은 치즈가 모두 녹을 때까지 반복한다.
while remain:
    answer += 1
    # 녹아서 없어질 치즈의 인덱스로, 근접한 칸 중 2칸 이상이 외부 공기라면 해당 치즈는 녹는다.
    remove = set()
    for i, j in remain:
        count = 0
        if paper[i-1][j] == -1:
            count += 1
        if paper[i+1][j] == -1:
            count += 1
        if paper[i][j-1] == -1:
            count += 1
        if paper[i][j+1] == -1:
            count += 1

        if count >= 2:
            remove.add((i, j))

    for i, j in remove:
        paper[i][j] = -1
        remain.remove((i, j))

    # 치즈가 녹아서 없어질때, 외부 공기와 접촉되는 내부 공기들을 찾는다.
    to_outer = set()
    for i, j in inner:
        if paper[i-1][j] == -1 or paper[i+1][j] == -1 or paper[i][j-1] == -1 or paper[i][j+1] == -1:
            to_outer.add((i, j))

    # 외부 공기와 접촉된 내부 공기들과 연결된 모든 내부 공기는 외부 공기가 된다.
    # bfs를 돌며 외부 공기에 노출된 내부 공기를 전부 없앤다.
    while to_outer:
        visited = [[False] * M for _ in range(N)]
        q = deque()
        i, j = to_outer.pop()
        q.append((i, j))
        visited[i][j] = True

        while q:
            i, j = q.popleft()
            if (i, j) in to_outer:
                to_outer.remove((i, j))
            inner.remove((i, j))
            paper[i][j] = -1

            if not visited[i-1][j] and paper[i-1][j] == 0:
                q.append((i-1, j))
                visited[i-1][j] = True

            if not visited[i][j-1] and paper[i][j-1] == 0:
                q.append((i, j-1))
                visited[i][j-1] = True

            if not visited[i+1][j] and paper[i+1][j] == 0:
                q.append((i+1, j))
                visited[i+1][j] = True

            if not visited[i][j+1] and paper[i][j+1] == 0:
                q.append((i, j+1))
                visited[i][j+1] = True

print(answer)
