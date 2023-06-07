from collections import deque

N, K = map(int, input().split())
dq = deque([i for i in range(1, N+1)])
jose_seq = []

while len(dq) > 0:
    dq.rotate(-K + 1)
    jose_seq.append(dq.popleft())

print('<', end='')
print(*jose_seq, sep=', ', end='')
print('>')