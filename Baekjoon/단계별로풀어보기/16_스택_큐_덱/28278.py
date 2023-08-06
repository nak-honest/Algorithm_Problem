import sys

stack = []
N = int(input())

for _ in range(N):
    commands = sys.stdin.readline().split()

    if commands[0] == '1':
        stack.append(commands[1])
    elif commands[0] == '3':
        print(len(stack))
    elif commands[0] == '4':
        print(int(len(stack) == 0))
    elif not stack:
        print(-1)
    elif commands[0] == '2':
        print(stack.pop())
    else:
        print(stack[-1])