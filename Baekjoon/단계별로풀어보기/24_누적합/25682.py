import sys

N, M, K = map(int, input().split())
board = [list(sys.stdin.readline().rstrip('\n')) for _ in range(N)]


white_start = [[0]*M for _ in range(N)]
black_start = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if (i + j) % 2 == 0 and board[i][j] == 'B':
            black_start[i][j] = 1
        elif (i + j) % 2 == 0 and board[i][j] == 'W':
            white_start[i][j] = 1
        elif board[i][j] == 'B':
            white_start[i][j] = 1
        else:
            black_start[i][j] = 1

white_dp = [[0]*(M+1) for _ in range(N+1)]
black_dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        white_dp[i][j] = white_start[i-1][j-1] + white_dp[i-1][j] + white_dp[i][j-1] - white_dp[i-1][j-1]
        black_dp[i][j] = black_start[i-1][j-1] + black_dp[i-1][j] + black_dp[i][j-1] - black_dp[i-1][j-1]

max_fill = 0

for i in range(K, N+1):
    for j in range(K, M+1):
        white_fill = white_dp[i][j] - white_dp[i-K][j] - white_dp[i][j-K] + white_dp[i-K][j-K]
        black_fill = black_dp[i][j] - black_dp[i-K][j] - black_dp[i][j-K] + black_dp[i-K][j-K]

        max_fill = max(max_fill, white_fill, black_fill)


print(K * K - max_fill)
