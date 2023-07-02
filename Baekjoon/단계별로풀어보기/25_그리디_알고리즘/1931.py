# 문제를 잘 읽자. 시작 시간과 끝나는 시간이 같지 않다는 조건이 없다.
# 회의를 시작하자마자 끝날수 있다는게 현실세계에서는 어색해 보이지만, 문제를 잘 읽어야 한다!

import sys

N = int(input())
meetings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 끝나는 시간이 빠른 순서대로 정렬.
# 끝나는 시간과 시작하는 시간이 같은 경우도 있기 때문에 끝나는 시간이 같다면 시작하는 시간이 느린 순서대로 정렬.
meetings.sort(key=lambda x: (x[1], x[0]))
cur_time = 0
count = 0

for meeting in meetings:
    if meeting[0] < cur_time:
        continue
    cur_time = meeting[1]

    count += 1

print(count)
