import sys

N = int(input())

# i ~ j 까지의 행렬을 곱하면 그 행렬은 mats[i][0] x mats[j][1] 의 행렬이 된다.
mats = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# dp[i][j] 는 i~j 까지의 행렬을 곱하는데 필요한 비용의 최솟값을 저장한다.
dp = [[0] * N for _ in range(N)]

for length in range(2, N+1):
    for start in range(N-length+1):
        min_cost = sys.maxsize
        # start ~ start + length - 1 까지의 행렬을 곱하는데 필요한 비용의 최솟값을 구한다.
        for sub_start in range(start+1, start+length):
            # start ~ start + length - 1 를 start ~ sub_start - 1 과 sub_start ~ start + length - 1 두개의 행렬 곱으로 쪼갠다.
            # 그중에서 최소 비용을 찾는다.
            min_cost = min(dp[start][sub_start-1] + dp[sub_start][start+length-1] + \
                       mats[start][0] * mats[sub_start][0] * mats[start+length-1][1], min_cost)

        dp[start][start+length-1] = min_cost

print(dp[0][N-1])
