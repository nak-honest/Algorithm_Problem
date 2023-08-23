import sys
from collections import deque

N = int(input())
A = []
F = dict()

# count() 를 이용해서 F를 업데이트하면 시간 초과가 발생한다. 원소를 하나씩 순회하면서 F를 업데이트 해야 시간 초과 발생 X.
for num in map(int, sys.stdin.readline().split()):
    A.append(num)
    F[num] = F.get(num, 0) + 1

NGF = [-1] * len(A)
stack = deque()

for i in range(len(A)):
    while stack and F[A[stack[-1]]] < F[A[i]]:
        NGF[stack.pop()] = A[i]

    stack.append(i)

print(*NGF)