import sys

def sum_dist(d1, d2):
    if d1 == sys.maxsize or d2 == sys.maxsize:
        return sys.maxsize

    return d1 + d2


N, M = map(int, input().split())

friend = [[sys.maxsize] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    friend[a][b] = 1
    friend[b][a] = 1

for i in range(1, N+1):
    friend[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            friend[i][j] = min(friend[i][j], sum_dist(friend[i][k], friend[k][j]))

min_kevin = sys.maxsize
answer = 1

for i in range(1, N+1):
    if sum(friend[i][1:]) < min_kevin:
        answer = i
        min_kevin = sum(friend[i][1:])

print(answer)
