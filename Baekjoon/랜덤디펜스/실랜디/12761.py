# 걸린 시간 : 15분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

from collections import deque

A, B, N, M = map(int, input().split())
visited = [False] * 100_001

q = deque()
q.append((N, 0))

diffs = [1, A, B, -1, -A, -B]

while q:
    node, count = q.popleft()

    if node == M:
        print(count)
        break

    for diff in diffs:
        if 0 <= node + diff <= 100_000 and not visited[node+diff]:
            q.append((node+diff, count+1))
            visited[node+diff] = True

    for mul in [A, B]:
        if node * mul <= 100_000 and not visited[node*mul]:
            q.append((node*mul, count+1))
            visited[node*mul] = True

