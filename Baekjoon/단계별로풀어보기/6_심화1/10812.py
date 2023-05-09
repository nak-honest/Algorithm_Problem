from collections import deque
N, M, *how = map(int, open(0).read().split())
answer = [i for i in range(1, N+1)]

for n in range(0, M*3, 3):
    i, j, k = how[n:n+3]
    # 해당 범위(i~j)만 deque의 rotate를 통해 회전시킨다.
    dq = deque(answer[i-1:j])
    dq.rotate(i-k)
    answer[i-1:j] = dq

print(*answer)