import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
NGE = [-1] * len(A)

stack = []

for i in range(len(A)):
    while stack and A[stack[-1]] < A[i]:
        NGE[stack[-1]] = A[i]
        stack.pop()
    stack.append(i)

print(*NGE)