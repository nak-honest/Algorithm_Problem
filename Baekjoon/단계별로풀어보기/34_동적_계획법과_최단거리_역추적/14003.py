# 12015 문제와 동일하게 푼다.
# 다만 cur_len의 중간 값들이 계속 업데이트 되기 때문에 실제 뒤에 있는 값은 앞에 있는 값과 같은 부분수열을 이룰수 없는 경우가 발생할 수 있다.
# 따라서 업데이트 될때 마다 이전 노드가 무엇이었는지를 저장해서, 마지막에 가장 긴 부분수열을 추적할 수 있도록 한다.

import sys
from bisect import bisect_left
from collections import deque

N = int(input())
A = list(map(int, sys.stdin.readline().split()))

# 이전 노드 저장
prev = [-1 for _ in range(N)]

cur_len = [(A[0], 0)]

for i in range(1, len(A)):
    if A[i] > cur_len[-1][0]:
        # 업데이트시 이전 노드 정보 저장
        prev[i] = cur_len[-1][1]
        cur_len.append((A[i], i))

    else:
        index = bisect_left(cur_len, (A[i], 0))
        # 업데이트시 이전 노드 정보 저장
        if index > 0:
            prev[i] = cur_len[index-1][1]

        cur_len[index] = (A[i], i)

print(len(cur_len))

answer = deque()
cur_index = cur_len[-1][1]

# 가장 긴 부분 수열을 추적한다.
while cur_index != -1:
    answer.appendleft(A[cur_index])
    cur_index = prev[cur_index]

print(*answer)