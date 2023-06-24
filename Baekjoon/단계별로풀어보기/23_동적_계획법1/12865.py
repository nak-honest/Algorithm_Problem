# 작년 알고리즘 수업 때 배운 유명한 냅색 문제
# 하지만 백트래킹 방식만 생각나고 dp 방식은 생각나지 않았다.
# dp 문제들을 더 많이 풀어보자.

import sys

N, K = map(int, input().split())
W, V = [0], [0]
for _ in range(N):
    weight, value = map(int, sys.stdin.readline().split())
    W.append(weight)
    V.append(value)

# dp[i][w]에는 1 ~ i 번 물건들 중에서만 골라서 가방에 넣을 수 있고, 최대 w의 무게까지만 가져갈 수 있을때의 최대 가치를 저장한다.
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for w in range(1, K+1):
        if W[i] > w:
            # i번 물건을 넣으면 무게를 초과하기 때문에 가져갈 수 없다.
            dp[i][w] = dp[i-1][w]
        else:
            # i번 물건을 가져갈때와 가져가지 않을때 중 더 가치가 높은 것을 택한다.
            dp[i][w] = max(dp[i-1][w], V[i] + dp[i-1][w-W[i]])

print(dp[N][K])