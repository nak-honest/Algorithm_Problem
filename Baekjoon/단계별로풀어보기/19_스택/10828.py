from collections import deque
import sys

# 직접 구현은 나중에 자바로 구현
N = int(input())
stack = deque()

for _ in range(N):
    line = sys.stdin.readline().split()
    command = line[0]
    argument = None
    if len(line) == 2:
        argument = line[1]

    if command == 'push':
        stack.append(argument)
    elif command == 'pop' and len(stack) != 0:
        print(stack.pop())
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(int(len(stack) == 0))
    elif command == 'top' and len(stack) != 0:
        print(stack[-1])
    else:
        print(-1)