# 걸린 시간 : 1시간 24분
# 제출 횟수 : 6번
# 풀이 참조 : x
# 반례 참조 : O

# 각 노드에서 리프노드까지 가는 최장 거리를 업데이트 하는 방식으로 해결하였는데
# 자식보다 부모 노드를 먼저 업데이트 해야 한다는 사실을 뒤늦게 깨달았다.
# 약간 프로그래머스 86971 문제(전력망을 둘로 나누기)와 비슷한 느낌으로 문제를 풀었다.
# 프로그래머스 문제를 풀때에는 자식 노드를 모두 업데이트한 것을 확인한 뒤에 부모 노드를 업데이트 하였는데, 이 문제를 풀땐 좀 늦게 알아차렸다.

import sys
from collections import deque
from copy import deepcopy

V = int(input())

adj_list = [[] for _ in range(V+1)]

# 먼저 인접 노드 정보를 업데이트 한다. 이때 정점 번호 순서대로 입력되지 않을 수 있음에 주의!
for _ in range(V):
    adj = list(map(int, sys.stdin.readline().split()))
    i = adj[0]
    adj = adj[1:]
    adj.pop()

    for j in range(len(adj) // 2):
        adj_list[i].append([adj[2*j], adj[2*j+1]])

# 1번 노드를 루트로 삼고 문제를 푼다.
root = 1

# 각 노드의 자식 노드들을 저장한다.
child = [[] for _ in range(V+1)]

# 각 노드의 부모 노드와 부모 노드 까지의 거리를 저장한다.
parent = [[-1, 0] for _ in range(V+1)]

# 리프노드들을 저장한다.
leafs = []

q = deque()
visited = [False] * (V+1)

visited[root] = True
q.append(root)

# 먼저 각 노드의 자식 노드 정보, 부모 노드 정보를 업데이트 한다.
while q:
    node = q.popleft()

    for next, dist in adj_list[node]:
        if not visited[next]:
            child[node].append(next)
            parent[next] = [node, dist]
            q.append(next)
            visited[next] = True

# 리프 노드들을 업데이트 한다.
for i in range(1, V+1):
    if not child[i]:
        leafs.append(i)

# 트리의 지름
max_diameter = 0

# 각 노드에서 갈수 있는 리프노드까지의 최장 거리를 저장한다.
# 이때 각 노드에서 부모노드를 통해서는 리프노드에 도달할 수 없다.
# 즉 해당 노드에서 밑으로만 갔을때의 리프노드까지의 최장 거리를 저장한다.
max_len_to_leaf = [0 for _ in range(V+1)]

q = deque(leafs)
visited = [False] * (V+1)

# max_len_to_leaf을 업데이트 할 때 자식 노드를 다 업데이트 하지 않은 경우 부모노드를 업데이트 하면 안된다.
# 따라서 모든 자식이 업데이트 되었는지 확인한 다음에 부모의 max_len_to_leaf을 업데이트 해야한다.
# 모든 자식이 업데이트 되었다면 rest_child는 비어있게 된다.
rest_child = deepcopy(child)

# max_len_to_leaf을 업데이트 하면서 트리의 지름도 업데이트 한다.
while q:
    node = q.popleft()
    largest = 0
    second_largest = 0

    # 자식 노드들의 max_len_to_leaf에 node 까지의 거리를 합한 것중 가장 큰 값과 두번째로 큰 값을 찾는다.
    # 이 노드를 공통 조상으로 하는 두 리프 노드 까지의 거리의 합은 두 노드 사이의 거리가 된다.
    # 이 노드의 자식의 max_len_to_leaf에 그 자식에서 node까지의 거리를 더한 값은 해당 자식을 통해 갈수 있는 리프노드까지의 최장거리가 된다.
    # 따라서 c1을 통해 갈 수 있는 최장 거리가 가장 길고, c2를 통해 갈수 있는 최장 거리가 그 다음으로 길다면
    # node가 최소 공통 조상인 리프노드 중 가장 거리가 긴 것은 c1과 c2사이의 거리이다.
    # 따라서 c1과 c2 사이의 거리가 max_diameter보다 크다면 max_diameter를 업데이트 한다.
    for c in child[node]:
        # cur_len은 자식 c를 통해 갈수 있는 리프노드 중 가장 먼 거리를 의미한다.
        cur_len = parent[c][1] + max_len_to_leaf[c]

        # node의 모든 자식들 중에서 리프노드까지의 거리가 가장 먼것과 두번쨰로 먼것을 업데이트 한다.
        if cur_len >= largest:
            second_largest = largest
            largest = cur_len
        elif cur_len >= second_largest:
            second_largest = cur_len

    # max_diameter를 업데이트하고, max_len_to_leaf도 업데이트 한다.
    max_diameter = max(max_diameter, largest + second_largest)
    max_len_to_leaf[node] = largest

    # node가 루트가 아니라면 rest_child에서 이 node를 삭제한다.
    # node의 max_len_to_leaf를 업데이트 완료했기 때문이다.
    if node != root:
        rest_child[parent[node][0]].remove(node)

    # 만약 node의 부모의 자식중 업데이트 하지 않은 자식이 더이상 없고, 큐에 아직 부모를 넣지 않았다면 큐에 부모를 넣는다.
    if not rest_child[parent[node][0]] and not visited[parent[node][0]] and parent[node][0] != -1:
        q.append(parent[node][0])
        visited[parent[node][0]] = True

print(max_diameter)
