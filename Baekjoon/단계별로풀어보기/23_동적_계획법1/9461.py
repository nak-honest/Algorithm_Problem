import sys

T = int(input())
cases = [int(sys.stdin.readline()) for _ in range(T)]

max_N = max(cases)
P = [0, 1, 1, 1, 2, 2] + [0]*(max_N - 5)

for k in range(6, max_N+1):
    P[k] = P[k-1] + P[k-5]

for N in cases:
    print(P[N])