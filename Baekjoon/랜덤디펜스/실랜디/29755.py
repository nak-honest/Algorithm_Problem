# 걸린 시간 : 25분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

import sys
from bisect import bisect_left

N, M = map(int, input().split())
blackhole = list(sorted(map(int, sys.stdin.readline().split())))
answer = 0

for _ in range(M):
    a, w = map(int, sys.stdin.readline().split())
    blackhole_index = bisect_left(blackhole, a)
    p = sys.maxsize
    if blackhole_index < N:
        p = min(p, abs(blackhole[blackhole_index] - a) * w)
    if blackhole_index - 1 >= 0:
        p = min(p, abs(blackhole[blackhole_index-1] - a) * w)

    answer = max(answer, p)

print(answer)

