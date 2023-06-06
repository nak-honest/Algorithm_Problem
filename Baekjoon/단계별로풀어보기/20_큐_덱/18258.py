import sys
from collections import deque

N = int(input())
queue = deque()

for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(int(len(queue) == 0))
    elif not queue:
        print(-1)
    elif command[0] == 'pop':
        print(queue.popleft())
    elif command[0] == 'front':
        print(queue[0])
    elif command[0] == 'back':
        print(queue[-1])
