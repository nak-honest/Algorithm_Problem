# 플로이드 와샬
import sys

def add(a, b):
    if a == sys.maxsize or b == sys.maxsize:
        return sys.maxsize
    else:
        return a + b

n = int(input())
m = int(input())

W = [[sys.maxsize] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    W[a][b] = min(W[a][b], c)

for i in range(n+1):
    W[i][i] = 0

for k in range(1, n+1):
    for i in range(n+1):
        for j in range(n+1):
            W[i][j] = min(W[i][j], add(W[i][k], W[k][j]))

for i in range(1, n+1):
    for j in range(1, n+1):
        if W[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(W[i][j], end=' ')
    print()