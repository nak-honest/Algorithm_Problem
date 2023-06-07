from collections import deque

N = int(input())
dq = deque([i for i in range(1, N+1)])

while len(dq) > 1:
    dq.popleft()
    dq.rotate(-1)

print(*dq)