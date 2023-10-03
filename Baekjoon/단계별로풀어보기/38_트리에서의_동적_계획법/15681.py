# 걸린 시간 : 19분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

# 1167 문제의 풀이와 비슷하다.
# 자식노드에서 루트노드로 올라가면서 서브트리의 노드 개수를 업데이트 한다.
# 자세한 풀이는 1167 풀이참조.

import sys
from collections import deque

N, R, Q = map(int, sys.stdin.readline().split())

adj_list = [[] for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, sys.stdin.readline().split())
    adj_list[U].append(V)
    adj_list[V].append(U)

parent = [-1] * (N+1)
child = [[] for _ in range(N+1)]
rest_child = [set() for _ in range(N+1)]
leaf = []
sub_count = [1] * (N+1)

q = deque()
visited = [False] * (N+1)
q.append(R)
visited[R] = True

while q:
    p = q.popleft()

    for c in adj_list[p]:
        if not visited[c]:
            child[p].append(c)
            rest_child[p].add(c)
            parent[c] = p
            q.append(c)
            visited[c] = True

for node in range(1, N+1):
    if not child[node]:
        leaf.append(node)

q = deque(leaf)

while q:
    p = q.popleft()
    for c in child[p]:
        sub_count[p] += sub_count[c]

    if p != R:
        rest_child[parent[p]].remove(p)

    if not rest_child[parent[p]] and p != R:
        q.append(parent[p])

for _ in range(Q):
    U = int(sys.stdin.readline())
    print(sub_count[U])

'''
       5
     4   6
    3   7 8 9
   1 2  
'''