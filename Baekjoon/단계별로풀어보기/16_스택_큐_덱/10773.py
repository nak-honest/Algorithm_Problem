import sys

K = int(input())
stack = []

for _ in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop()
        continue

    stack.append(num)

print(sum(stack))