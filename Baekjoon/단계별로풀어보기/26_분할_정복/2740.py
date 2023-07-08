import sys

N, M = map(int, input().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

M, K = map(int, input().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

answer = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            answer[i][j] += A[i][k] * B[k][j]

for row in answer:
    print(*row)