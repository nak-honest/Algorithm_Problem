# 처음에 메모리를 신경을 안써서 초과가 자주 났다.
# 그 후에는 N=1인 경우에 엣지 케이스라서 한번 더 틀렸다.
# 문제도 꼼꼼하게(시간 및 메모리 체크), 엣지 케이스도 한번 더 생각하자!!

# 걸린 시간 : 20분
# 제출 횟수 : 5번
# 풀이 참조 : x
# 반례 참조 : x

import sys

N = int(input())
first_board = list(map(int, sys.stdin.readline().split()))

# 메모리를 초과하지 않기 위해 range(2) 만 사용한다.
# dp[0]가 이전 줄의 최대, 최소값이고 dp[1]이 현재 줄의 최대, 최소값이다.
max_dp = [[0, 0, 0] for _ in range(2)]
min_dp = [[0, 0, 0] for _ in range(2)]

# N=1 인 경우를 위해 dp[1]에도 값을 업데이트한다.
max_dp[0] = first_board.copy()
max_dp[1] = first_board.copy()
min_dp[0] = first_board.copy()
min_dp[1] = first_board.copy()

for _ in range(N-1):
    # 각 줄도 메모리에 한번에 저장하지 않고, for문을 돌면서 하나씩 가져온다.
    board = list(map(int, sys.stdin.readline().split()))
    max_dp[1][0] = max(max_dp[0][0], max_dp[0][1]) + board[0]
    max_dp[1][1] = max([max_dp[0][0], max_dp[0][1], max_dp[0][2]]) + board[1]
    max_dp[1][2] = max(max_dp[0][1], max_dp[0][2]) + board[2]

    min_dp[1][0] = min(min_dp[0][0], min_dp[0][1]) + board[0]
    min_dp[1][1] = min([min_dp[0][0], min_dp[0][1], min_dp[0][2]]) + board[1]
    min_dp[1][2] = min(min_dp[0][1], min_dp[0][2]) + board[2]

    max_dp[0] = max_dp[1].copy()
    min_dp[0] = min_dp[1].copy()


print(max(max_dp[1]), min(min_dp[1]))