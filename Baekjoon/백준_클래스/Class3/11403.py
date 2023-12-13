import sys

N = int(input())

W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 플로이드 알고리즘으로 i -> j 의 경로가 존재하는지 찾는다.
for k in range(N):
    for i in range(N):
        for j in range(N):
            if W[i][k] != 0 and W[k][j] != 0:
                W[i][j] = 1

for i in range(N):
    print(*W[i])
