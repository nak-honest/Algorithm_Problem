# 걸린 시간 : 15분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

import sys

def add_dist(p, q):
    if p == sys.maxsize or q == sys.maxsize:
        return sys.maxsize

    return p + q

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))

graph = [[sys.maxsize] * (n+1) for _ in range(n+1)]
dp = [[sys.maxsize] * (n+1) for _ in range(n+1)]


for i in range(1, n+1):
    graph[i][i] = 0
    dp[i][i] = 0

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a][b] = l
    graph[b][a] = l
    dp[a][b] = l
    dp[b][a] = l

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i][j], add_dist(dp[i][k], dp[k][j]))

answer = 0
for i in range(1, n+1):
    item_count = 0

    for j in range(1, n+1):
        if dp[i][j] <= m:
            item_count += items[j]

    answer = max(answer, item_count)

print(answer)