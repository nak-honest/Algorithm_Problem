from collections import deque

N, M = map(int, input().split())
dq = deque([i for i in range(1, N+1)])
locations = list(map(int, input().split()))
rotate_cnt = 0

for loc in locations:
    index = dq.index(loc)
    if index >= len(dq) - index:
        rotate_cnt += len(dq) - index
        dq.rotate(len(dq) - index)
        dq.popleft()
    else:
        rotate_cnt += index
        dq.rotate(-index)
        dq.popleft()

print(rotate_cnt)