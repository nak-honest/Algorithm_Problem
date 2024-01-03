# N == K 인 경우 엣지 케이스로 적용된다.

# 걸린 시간 : 25분
# 제출 횟수 : 2번
# 풀이 참조 : x
# 반례 참조 : x

import sys
from collections import deque

N, K = map(int, input().split())
q = deque()
q.append((N, 0))

# min_count에는 해당 숫자로 이동하는데 필요한 최소한의 카운트를 저장한다.
min_count = [sys.maxsize] * (2 * max(N, K) + 1)
min_count[N] = 0
answer_count = sys.maxsize
case = 0

# 엣지 케이스
if N == K:
    answer_count = 0

# bfs를 돌며 각 숫자에 가는데 필요한 최소한의 카운트를 구한다.
while q:
    node, count = q.popleft()

    if node == K and count == answer_count:
        case += 1

    if answer_count <= count:
        continue

    if node - 1 >= 0 and min_count[node-1] >= count+1:
        min_count[node-1] = count+1
        q.append((node-1, count+1))
        if node - 1 == K:
            answer_count = count+1

    if node + 1 <= K and min_count[node+1] >= count+1:
        min_count[node+1] = count+1
        q.append((node+1, count+1))
        if node + 1 == K:
            answer_count = count+1

    if node * 2 <= 2*K and min_count[node*2] >= count+1:
        min_count[node*2] = count+1
        q.append((node*2, count+1))
        if node * 2 == K:
            answer_count = count+1


print(answer_count, case, sep='\n')