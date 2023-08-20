'''
dp[i][c] = 0 ~ (i-1) 의 앱중에서 최대 c의 비용으로 만들수 있는 최대 메모리

if C[i] > c,  dp[i][c] = dp[i-1][c]
else,         dp[i][c] = max(dp[i-1][c], dp[i-1][c-C[i]] + A[i])

M 바이트를 확보하기 위한 최소 비용은 dp[N][c] >= M 이 되는 가장 작은 c이다.
'''

import sys

N, M = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))
C = list(map(int, sys.stdin.readline().split()))

total_c = sum(C)

dp = [[0] * (total_c+1) for _ in range(N+1)]

for i in range(1, N+1):
    for c in range(1, total_c+1):
        if C[i-1] > c:
            dp[i][c] = dp[i-1][c]
        else:
            dp[i][c] = max(dp[i-1][c], dp[i-1][c-C[i-1]] + A[i-1])

for c in range(1, total_c+1):
    if dp[N][c] >= M:
        print(c)
        break