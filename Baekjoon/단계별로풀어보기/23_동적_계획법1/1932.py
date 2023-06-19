import sys

n = int(input())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
routes = [[0] * i for i in range(1, n+1)] # 삼각형에서 각 자리까지 오는 경로의 최대값 저장

for i in range(n):
    for j in range(i+1):
        if j - 1 < 0: # 왼쪽 대각선 위가 없는 경우
            routes[i][j] = routes[i-1][j] + triangle[i][j]
        elif j > i - 1: # 오른쪽 대각선 위가 없는 경우
            routes[i][j] = routes[i-1][j-1] + triangle[i][j]
        else:
            routes[i][j] = max(routes[i-1][j-1], routes[i-1][j]) + triangle[i][j]

print(max(routes[n-1]))