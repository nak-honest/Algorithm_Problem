import sys
from collections import deque

for _ in range(int(input())):
    l = int(input())
    knight = list(map(int, sys.stdin.readline().split()))
    dest = list(map(int, sys.stdin.readline().split()))

    # bfs를 돌며 최단 경로를 찾는다.
    q = deque()
    visited = [[False] * l for _ in range(l)]

    q.append((knight, 0))
    visited[knight[0]][knight[0]] = True

    while q:
        node, count = q.popleft()

        if node[0] == dest[0] and node[1] == dest[1]:
            print(count)
            break

        next = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        for x, y in next:
            if 0 <= node[0] + x < l and 0 <= node[1] + y < l and not visited[node[0]+x][node[1]+y]:
                visited[node[0]+x][node[1]+y] = True
                q.append(((node[0]+x, node[1]+y), count+1))
