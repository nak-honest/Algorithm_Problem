from bisect import bisect_left
import sys

N = int(input())
A = sorted(list(map(int, sys.stdin.readline().split())))
M = int(input())
num = list(map(int, sys.stdin.readline().split()))

print(*[int(bisect_left(A, n) < N and A[bisect_left(A, n)] == n) for n in num], sep='\n')