import sys
from collections import deque

N = int(input())
cur_line = deque(map(int, sys.stdin.readline().split()))
stack = []
next_num = 1

while cur_line:
    first = cur_line.popleft()
    if first == next_num:
        next_num += 1
        while stack and stack[-1] == next_num:
            stack.pop()
            next_num += 1
    else:
        stack.append(first)

if stack:
    print("Sad")
else:
    print("Nice")