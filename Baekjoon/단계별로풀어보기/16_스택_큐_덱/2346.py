import sys
from collections import deque

N = int(input())


dq = deque(enumerate(map(int, sys.stdin.readline().split())))


while dq:
    num, next = dq.popleft()
    print(num+1, end=' ')

    if next > 0:
        dq.rotate(-next+1)
    else:
        dq.rotate(-next)
