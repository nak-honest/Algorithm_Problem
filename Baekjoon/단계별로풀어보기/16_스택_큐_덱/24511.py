# 스택은 넘어 오는 값을 그대로 넘긴다.
# 큐는 자신의 값을 왼쪽 큐로 옮긴다.
# 마지막 큐에 있는 값은 옮겨질 곳이 없기 때문에 그 값이 리턴된다.
# 따라서 스택은 없애고 큐만 남겨놓고 왼쪽에 값을 넣고 오른쪽에 있는 값을 pop해서 리턴하면 된다.

import sys
from collections import deque

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

dq = deque([B[i] for i in range(N) if A[i] == 0])

M = int(input())
C = list(map(int, sys.stdin.readline().split()))

for c in C:
    dq.appendleft(c)
    print(dq.pop(), end=' ')