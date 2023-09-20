# 걸린 시간 : 11분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

# 1167 문제와 완전히 동일하다. 처음부터 대놓고 부모 자식 노드 정보를 알려주기 때문에 좀더 쉽다.
# 풀이는 동일!
import sys
from collections import deque

n = int(input())
root = 1

parent = [[-1, 0] for _ in range(n+1)]
child = [[] for _ in range(n+1)]
rest_child = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c, w = map(int, sys.stdin.readline().split())
    child[p].append(c)
    rest_child[p].append(c)
    parent[c] = [p, w]

leafs = []

for i in range(1, n+1):
    if not child[i]:
        leafs.append(i)

max_len_to_leaf = [0] * (n+1)
q = deque(leafs)
visited = [False] * (n+1)

answer = 0

while q:
    node = q.popleft()
    max_len = 0
    second_max_len = 0

    for c in child[node]:
        cur_len = max_len_to_leaf[c] + parent[c][1]

        if cur_len >= max_len:
            second_max_len = max_len
            max_len = cur_len
        elif cur_len > second_max_len:
            second_max_len = cur_len

    max_len_to_leaf[node] = max_len
    answer = max(answer, max_len + second_max_len)

    if node == root:
        break

    p = parent[node][0]

    rest_child[p].remove(node)

    if not rest_child[p] and not visited[p]:
        q.append(p)
        visited[p] = True

print(answer)