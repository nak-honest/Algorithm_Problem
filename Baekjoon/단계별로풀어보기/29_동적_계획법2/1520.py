import sys

# max_i, max_j 에 plus만큼 경로의 개수가 업데이트 되었을때, max_i, max_j 를 지나서 새로 생기는 경로의 개수를 업데이트한다.
# 이때 dp의 값은 max_i, max_j 까지 가는 경로만 업데이트 되기 때문에, 이 범위를 벗어나지 않는 선에서만 업데이트 한다.
def find_back_path(i, j, max_i, max_j, plus):
    # 위로 가는 경로가 존재한다면 업데이트 후, 위의 칸에 대해서 재귀적으로 새로운 경로를 업데이트 한다.
    # 재귀적으로 업데이트 하는 이유는 max_i, max_j 를 통해 새로 생기는 경로는 주변으로 퍼지면서 업데이트 되기 때문이다.
    if i - 1 >= 0 and maps[i][j] > maps[i-1][j]:
        dp[i-1][j] += plus
        find_back_path(i-1, j, max_i, max_j, plus)
    # 왼쪽으로 가는 경로가 존재한다면 업데이트 후, 왼쪽 칸에 대해서 재귀적으로 새로운 경로를 업데이트 한다.
    if j - 1 >= 0 and maps[i][j] > maps[i][j-1]:
        dp[i][j-1] += plus
        find_back_path(i, j-1, max_i, max_j, plus)

    # max_i, max_j 범위를 벗어나지 않는 선에서, 아래로 가는 경로가 존재한다면 재귀적으로 새로운 경로를 업데이트 한다.
    if i + 1 < max_i or (i + 1 == max_i and j <= max_j):
        if maps[i][j] > maps[i+1][j]:
            dp[i+1][j] += plus
            find_back_path(i+1, j, max_i, max_j, plus)

    # max_i, max_j 범위를 벗어나지 않는 선에서, 오른쪽으로 가는 경로가 존재한다면 재귀적으로 새로운 경로를 업데이트 한다.
    if (i == max_i and j + 1 <= max_j) or (i < max_i and j + 1 < N):
        if maps[i][j] > maps[i][j+1]:
            dp[i][j+1] += plus
            find_back_path(i, j+1, max_i, max_j, plus)


M, N = map(int, input().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

# dp[i][j] 에는 dp[0][0]을 시작으로 갈수 있는 경로의 수를 저장한다.
# 이때 이중 for 문으로 i와 j가 1씩 증가하면서 먼저는 dp[i][j]를 업데이트 하고,
# i, j 를 거쳐서 갈수 있는 새로운 경로가 존재한다면 이전의 dp 값을 업데이트한다.
dp = [[0] * N for _ in range(M)]
dp[0][0] = 1

for i in range(M):
    for j in range(N):
        # 먼저는 dp[i][j]의 값을 업데이트한다.

        # i-1, j 를 거쳐서 i, j 로 올 수 있다면 i-1, j 까지의 경로의 개수를 더한다.
        # 이는 i, j 바로 상단에서 i, j 로 오는 경로의 개수를 의미한다.
        if i - 1 >= 0 and maps[i][j] < maps[i-1][j]:
            dp[i][j] += dp[i-1][j]
        # i, j-1 를 거쳐서 i, j 로 올 수 있다면 i, j-1 까지의 경로의 개수를 더한다.
        # 이는 i, j 바로 왼쪽에서 i, j 로 오는 경로의 개수를 의미한다.
        if j - 1 >= 0 and maps[i][j] < maps[i][j-1]:
            dp[i][j] += dp[i][j-1]

        # 만약 dp[i][j]의 값이 업데이트 되었다면 i, j 를 거쳐서 이전 칸으로 가는 새로운 경로가 있는지 확인한다.
        # 이때 새로운 경로의 개수는 i, j로 가는 경로의 개수이다.
        if dp[i][j] != 0:
            find_back_path(i, j, i, j, dp[i][j])

print(dp[M-1][N-1])

'''
오른쪽으로 한칸 씩 이동, 오른쪽 끝에서는 바로 밑칸의 가장 왼쪽으로 이동.
그렇게 이동하면서 해당 칸에 갈수 있는 경로의 수를 세고, 그 경로를 거쳐서 이전의 칸들에 갈 수 있는지도 본다.
'''