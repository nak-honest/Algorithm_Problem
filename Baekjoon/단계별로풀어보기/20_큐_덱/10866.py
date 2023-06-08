from collections import deque
import sys

N = int(input())
dq = deque()

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        dq.appendleft(command[1])
    elif command[0] == 'push_back':
        dq.append(command[1])
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        print(int(len(dq) == 0))
    elif len(dq) == 0:
        print(-1)
    elif command[0] == 'pop_front':
        print(dq.popleft())
    elif command[0] == 'pop_back':
        print(dq.pop())
    elif command[0] == 'front':
        print(dq[0])
    elif command[0] == 'back':
        print(dq[-1])