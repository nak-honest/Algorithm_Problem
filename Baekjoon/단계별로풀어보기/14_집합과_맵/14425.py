import sys

N, M = map(int, input().split())
S = {sys.stdin.readline().rstrip('\n'): 0 for _ in range(N)}
strings = [sys.stdin.readline().rstrip('\n') for _ in range(M)]

print(len(list(filter(lambda s: s in S, strings))))