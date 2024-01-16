# 보조 PD에게 배정되지 않은 가수가 있을 줄은 상상도 못했다..
# 문제가 좀 더 친절했으면 좋겠지만,, 내가 알아서 판단해야 한다.
# 문제에서 명확하게 나오지 않는 부분도 고려하는 연습을 해야 할 것 같다.

# 위상 정렬을 몰라서 좀 다르게 풀었다. 위상 정렬이 더 빠르고, 코드도 더 짧다!

# 걸린 시간 : 1시간
# 제출 횟수 : 8번
# 풀이 참조 : x
# 반례 참조 : O

import sys

N, M = map(int, input().split())

orders = [list(map(int, sys.stdin.readline().split()))[1:] for _ in range(M)]
# is_after[i][j]가 True 면, i가 j보다 뒷 순서라는 것이다.
is_after = [[False] * (N+1) for _ in range(N+1)]

for order in orders:
    for i in range(len(order)):
        for j in range(i+1, len(order)):
            is_after[order[j]][order[i]] = True

visited = [False] * (N+1)
# 각 보조 PD들이 담당하고 있는 가수들 중 아직 순서에 배정되지 않은 첫번째 가수를 가리킨다.
cur_index = [0] * M
# 아직 순서에 배정되지 않은 가수를 담당 중인 보조 PD들을 모아 놓는다.
remain_pd = list(range(M))

answer = []

# 각 보조 PD가 담당 중인 가수 중 가장 맨 앞에 와야 하는 가수를 찾는다.
while remain_pd:
    pd = remain_pd[0]

    while cur_index[pd] < len(orders[pd]) and visited[orders[pd][cur_index[pd]]]:
        cur_index[pd] += 1

    if cur_index[pd] == len(orders[pd]):
        remain_pd.remove(pd)
        continue

    first_singer = orders[pd][cur_index[pd]]
    removed_pd = []

    for pd in remain_pd:
        while cur_index[pd] < len(orders[pd]) and visited[orders[pd][cur_index[pd]]]:
            cur_index[pd] += 1

        if cur_index[pd] == len(orders[pd]):
            removed_pd.append(pd)

    for pd in removed_pd:
        remain_pd.remove(pd)

    prev_first_singer = -1
    while prev_first_singer != first_singer:
        prev_first_singer = first_singer
        for pd in remain_pd:
            cur_singer = orders[pd][cur_index[pd]]
            if is_after[first_singer][cur_singer]:
                first_singer = cur_singer

    answer.append(first_singer)
    visited[first_singer] = True

can_order = True
for i in range(len(answer)):
    for j in range(i+1, len(answer)):
        if is_after[answer[i]][answer[j]]:
            can_order = False
            break

for i in range(1, N+1):
    if not visited[i]:
        answer.append(i)

if can_order:
    print(*answer, sep='\n')
else:
    print(0)


'''
# 위상 정렬로 푼 풀이
import sys
from collections import deque

N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
in_degree = [0] * (N+1)

for _ in range(M):
    order = list(map(int, sys.stdin.readline().split()))[1:]

    for i in range(len(order)-1):
        adj_list[order[i]].append(order[i+1])
        in_degree[order[i+1]] += 1

visited = [False] * (N+1)
q = deque()
answer = []

for i in range(1, N+1):
    if in_degree[i] == 0:
        q.append(i)
        visited[i] = True

while q:
    singer = q.popleft()
    answer.append(singer)

    for next_singer in adj_list[singer]:
        if not visited[next_singer]:
            in_degree[next_singer] -= 1
            if in_degree[next_singer] == 0:
                q.append(next_singer)
                visited[next_singer]

if len(answer) != N:
    print(0)
else:
    print(*answer, sep='\n')
'''

