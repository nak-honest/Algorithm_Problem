# 걸린 시간 : 30분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

import sys

N = int(input())
home = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
count = [[[0] * N for _ in range(N)] for _ in range(3)]
count[0][0][1] = 1


for i in range(N):
    for j in range(N):
        if j + 1 < N and home[i][j+1] == 0:
            count[0][i][j+1] += count[0][i][j]
            count[0][i][j+1] += count[2][i][j]

        if i + 1 < N and home[i+1][j] == 0:
            count[1][i+1][j] += count[1][i][j]
            count[1][i+1][j] += count[2][i][j]

        if i + 1 < N and j + 1 < N and home[i][j+1] == 0 and home[i+1][j] == 0 and home[i+1][j+1] == 0:
            count[2][i+1][j+1] += count[0][i][j]
            count[2][i+1][j+1] += count[1][i][j]
            count[2][i+1][j+1] += count[2][i][j]

print(count[0][N-1][N-1] + count[1][N-1][N-1] + count[2][N-1][N-1])


'''
오른쪽, 아래, 오른쪽 아래 3칸
'''
