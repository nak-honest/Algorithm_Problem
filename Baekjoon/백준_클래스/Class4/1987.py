# pypy3로만 통과함. bfs로 풀면 python3로 통과 가능.

# 걸린 시간 : 40분
# 제출 횟수 : 3번
# 풀이 참조 : x
# 반례 참조 : x

import sys

R, C = map(int, input().split())
board = [list(sys.stdin.readline().rstrip('\n')) for _ in range(R)]
visited = {chr(i): False for i in range(65, 91)}

alpha_set = set()
for i in range(R):
    for j in range(C):
        alpha_set.add(board[i][j])

answer = 0

stack = []
stack.append([0, 0, 1])

while stack:
    i, j, count = stack[-1]
    answer = max(answer, count)

    if answer == len(alpha_set):
        break

    if visited[board[i][j]]:
        visited[board[i][j]] = False
        stack.pop()
        continue

    visited[board[i][j]] = True

    if i - 1 >= 0 and not visited[board[i-1][j]]:
        stack.append([i-1, j, count+1])

    if i + 1 < R and not visited[board[i+1][j]]:
        stack.append([i+1, j, count+1])

    if j - 1 >= 0 and not visited[board[i][j-1]]:
        stack.append([i, j-1, count+1])

    if j + 1 < C and not visited[board[i][j+1]]:
        stack.append([i, j+1, count+1])


print(answer)
