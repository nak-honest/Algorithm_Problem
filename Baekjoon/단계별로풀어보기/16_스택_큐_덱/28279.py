import sys
from collections import deque

N = int(input())
dq = deque()

for _ in range(N):
    commands = sys.stdin.readline().split()

    if commands[0] == '1':
        dq.appendleft(commands[1])
    elif commands[0] == '2':
        dq.append(commands[1])
    elif commands[0] == '5':
        print(len(dq))
    elif commands[0] == '6':
        print(int(len(dq) == 0))
    elif not dq:
        print(-1)
    elif commands[0] == '3':
        print(dq.popleft())
    elif commands[0] == '4':
        print(dq.pop())
    elif commands[0] == '7':
        print(dq[0])
    elif commands[0] == '8':
        print(dq[-1])