# 걸린 시간 : 10분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

import sys
from heapq import heappush
from heapq import heappop

N, M = map(int, input().split())

in_degree = [0] * (N+1)
adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    adj_list[A].append(B)
    in_degree[B] += 1

heap = []
answer = []
visited = [False] * (N+1)

for node in range(1, N+1):
    if in_degree[node] == 0:
        heappush(heap, node)
        visited[node] = True

while heap:
    node = heappop(heap)
    answer.append(node)

    for next in adj_list[node]:
        if not visited[next] and in_degree[next] != 0:
            in_degree[next] -= 1
            if in_degree[next] == 0:
                heappush(heap, next)
                visited[next] = True

print(*answer)