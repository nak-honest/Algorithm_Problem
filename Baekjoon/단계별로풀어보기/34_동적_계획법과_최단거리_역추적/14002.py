import sys
from collections import deque

N = int(input())
A = list(map(int, sys.stdin.readline().split()))

# 부분 수열의 길이 뿐만 아니라 이전 노드의 인덱스도 같이 저장한다.
# 나머지는 기본 LIS 문제랑 동일하다.
# 이전 노드의 인덱스가 -1이라는 것은 앞 노드가 없다는 것을 의미한다.
# 즉 그 노드가 증가하는 부분수열의 첫번째 원소라는 의미이다.
dp = [[1, -1] for _ in range(N)]

end_index = 0
answer_len = 1

for i in range(1, N):
    max_len = 0
    max_j = -1

    for j in range(i):
        if A[i] > A[j] and dp[j][0] > max_len:
            max_len = dp[j][0]
            max_j = j

    dp[i][0] = max_len + 1
    dp[i][1] = max_j

    if max_len + 1 > answer_len:
        answer_len = max_len + 1
        end_index = i

q = deque()
cur_index = end_index

# 이전 노드를 저장한 것을 기반으로 역추적을 한다.
while cur_index != -1:
    q.appendleft(A[cur_index])
    cur_index = dp[cur_index][1]

print(answer_len)
print(*q)
