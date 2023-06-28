# dp말고 각 행별로 누적합을 더하는 방식을 택했더니 시간초과가 발생했다.
# pypy3로 돌아가기는 했으나 더 효율적인 풀이는 dp를 이용한 풀이였다.

import sys

N, M = map(int, input().split())

table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# dp[i][j] 에는 x1 = 1, y1 = 1, x2 = i, y2 = j 일때의 누적합을 저장한다.
# 즉 (1, 1) ~ (i, j) 의 정사각형에 포함된 모든 수를 더한 값을 저장한다.
dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        # 위 쪽의 정사각형(dp[i][j+1]과 왼쪽의 정사각형(dp[i+1][j])을 더하면 왼쪽 대각선 위의 정사각형(dp[i][j])이 중복되어서 더해진다.
        # 따라서 왼쪽 대각선 위의 정사각형의 누적합인 dp[i][j]를 빼는 것이다.
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + table[i][j]


for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    # (1, 1) ~ (x2, y2) 까지의 큰 정사각형(dp[x2][y2])에서
    # 위 쪽의 정사각형(dp[x1-1][y2])과 왼쪽의 정사각형(dp[x2][y1-1])을 뺴면
    # 왼쪽 대각선 위의 정사각형(dp[x1-1][y1-1])이 중복으로 빼진다.
    # 따라서 왼쪽 대각선 위인 dp[x1-1][y1-1]을 더해준다.
    sum_table = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(sum_table)


'''
# 밑의 코드는 pypy3로는 풀리지만 python3로는 시간초과가 발생한다.
import sys

N, M = map(int, input().split())

table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

S = [[0] for _ in range(N)]

for i in range(N):
    for j in range(N):
        S[i].append(S[i][-1] + table[i][j])

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    sum_table = 0

    for i in range(x1-1, x2):
        sum_table += (S[i][y2] - S[i][y1-1])

    print(sum_table)

'''