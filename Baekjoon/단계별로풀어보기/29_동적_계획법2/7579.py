# 재채점으로 인해 오답이 되었다. 따라서 다시 풀었다.
# 배낭 문제에서 dp[i][c]는 최대 무게 c를 넘기지 않으면서, 1 ~ i 까지의 물건들로 만들수 있는 최대 비용을 의미한다.
# 현재 문제에서도 최대 비용 c를 넘기지 않으면서, 1 ~ i 까지의 앱들로 만들 수 있는 최대 비용을 dp[i][c]에 저장한다.
# 즉 dp[N][c]가 M보다 크다면, 비용 c로 M보다 큰 바이크를 확보할 수 있다는 것을 의미한다.
# 따라서 dp[N][c] >= M 을 만족하는 c의 최솟값이 정답이 된다.

import sys

N, M = map(int, input().split())

m = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

# 배낭 문제랑 똑같이 dp 값을 구한다.
dp = [[0] * (sum(c) + 1) for _ in range(N+1)]

for i in range(1, N+1):
    for cost in range(sum(c)+1):
        if c[i-1] <= cost:
            dp[i][cost] = max(dp[i-1][cost], dp[i-1][cost-c[i-1]] + m[i-1])
        else:
            dp[i][cost] = dp[i-1][cost]

# dp[N][cost] >= M 을 만족하는 최소 cost를 구한다.
for cost in range(sum(c)+1):
    if dp[N][cost] >= M:
        print(cost)
        break