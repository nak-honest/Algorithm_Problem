# 처음엔 브루트포스로 풀었다. 시간초과가 되지는 않았지만, 너무 많은 시간이 걸렸다.
# 따라서 dfs + branch 로 푸니 훨씬 적은 시간이 걸렸다.

# 걸린 시간 : 20분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

import sys

def dfs(i, j, depth, cur_sum):
    global answer
    if depth == 4:
        answer = max(answer, cur_sum)
        return
    if cur_sum + max_val * (4 - depth) <= answer:
        return

    for i_diff, j_diff in udlr:
        if i + i_diff < 0 or i + i_diff >= N or j + j_diff < 0 or j + j_diff >= M or visited[i+i_diff][j+j_diff]:
            continue

        if depth == 2:
            visited[i + i_diff][j + j_diff] = True
            dfs(i, j, depth + 1, cur_sum + paper[i+i_diff][j+j_diff])
            visited[i + i_diff][j + j_diff] = False

        visited[i+i_diff][j+j_diff] = True
        dfs(i+i_diff, j+j_diff, depth+1, cur_sum + paper[i+i_diff][j+j_diff])
        visited[i+i_diff][j+j_diff] = False


N, M = map(int, input().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
udlr = [(-1, 0), (1, 0), (0, -1), (0, 1)]

max_val = 0
for i in range(N):
    max_val = max(max_val, max(paper[i]))

answer = 0

for _i in range(N):
    for _j in range(M):
        visited[_i][_j] = True
        dfs(_i, _j, 1, paper[_i][_j])
        visited[_i][_j] = False

print(answer)

'''
shapes = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(2, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (0, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 2), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 1), (1, 0), (1, 1), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (0, 1), (0, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 1), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(1, 0), (0, 1), (1, 1), (2, 1)]
]

N, M = map(int, input().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = 0
for shape in shapes:
    i0, j0 = shape[0]
    i1, j1 = shape[1]
    i2, j2 = shape[2]
    i3, j3 = shape[3]

    for i in range(N):
        for j in range(M):
            part_sum = 0
            if i0 + i >= N or j0 + j >= M:
                continue
            part_sum += paper[i0 + i][j0 + j]

            if i1 + i >= N or j1 + j >= M:
                continue
            part_sum += paper[i1 + i][j1 + j]

            if i2 + i >= N or j2 + j >= M:
                continue
            part_sum += paper[i2 + i][j2 + j]

            if i3 + i >= N or j3 + j >= M:
                continue
            part_sum += paper[i3 + i][j3 + j]

            answer = max(answer, part_sum)

print(answer)
'''