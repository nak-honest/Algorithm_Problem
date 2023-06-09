import sys
from collections import deque

T = int(input())

for _ in range(T):
    p = sys.stdin.readline().rstrip('\n')
    n = int(input())
    dq = deque()
    seq = sys.stdin.readline().lstrip('[').rstrip(']\n').split(',')

    if n != 0:
        dq = deque(map(int, seq))

    is_reverse = False
    is_error = False

    for command in p.replace('RR', ''):
        if command == 'R':
            is_reverse = not is_reverse
        elif not dq:
            is_error = True
            break
        elif is_reverse:
            dq.pop()
        else:
            dq.popleft()

    if is_error:
        print('error')
    else:
        print('[', end='')
        if is_reverse:
            print(*reversed(dq), sep=',', end='')
        else:
            print(*dq, sep=',', end='')
        print(']')