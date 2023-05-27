import sys

N, M = map(int, input().split())
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

print(len(A | B) - len(A & B))