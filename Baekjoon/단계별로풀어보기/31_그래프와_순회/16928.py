import sys
from collections import deque

N, M = map(int, input().split())
ladder = dict()
snake = dict()

for _ in range(N):
    x, y = list(map(int, sys.stdin.readline().split()))
    ladder[x] = y

for _ in range(M):
    u, v = list(map(int, sys.stdin.readline().split()))
    snake[u] = v

q = deque()
visited = [False] * 101

q.append((1, 0))
visited[1] = True

# bfs를 돌며 count를 1씩 증가시킬때 갈수 있는 모든 칸을 확인한다.
while q:
    node, count = q.popleft()

    if node == 100:
        print(count)
        break

    for i in range(1, 7):
        next = node + i
        if next <= 100 and not visited[next]:
            visited[next] = True

            # 사다리가 있는 경우
            if next in ladder:
                q.append((ladder[next], count+1))
                visited[ladder[next]] = True
            # 뱀이 있는 경우
            if next in snake:
                q.append((snake[next], count+1))
                visited[snake[next]] = True
            # 사다리나 뱀 둘다 없는 경우
            else:
                q.append((next, count+1))
