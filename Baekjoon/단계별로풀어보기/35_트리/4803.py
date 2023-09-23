# 걸린 시간 : 40분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x


import sys
from collections import deque


for tc in range(1, sys.maxsize):
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    adj_list = [[] for _ in range(N+1)]

    for _ in range(M):
        i, j = map(int, sys.stdin.readline().split())
        adj_list[i].append(j)
        adj_list[j].append(i)

    visited = [False] * (N+1)
    parent = [-1] * (N+1)
    tree_count = 0

    # 트리의 개수를 센다.
    while True:
        # 이번에 확인할 트리의 루트 노드를 찾는다. 즉 아직 방문하지 않은 노드 중 가장 작은 노드를 찾는다.
        root = 0
        for i in range(1, N+1):
            if not visited[i]:
                root = i

        # 아직 방문하지 않은 노드가 없다는 것은 모든 노드를 방문했다는 것이므로, 트리의 개수를 전부 센 것이다.
        if root == 0:
            break

        # root를 루트노드로 삼을때 트리인지를 is_tree에 저장한다.
        is_tree = True

        # root 노드를 시작으로 탐색을 돌린다.
        q = deque()
        q.append(root)
        visited[root] = True

        while q:
            node = q.popleft()

            # node와 인접한 노드들 중 node의 부모를 제외하고는 모두 node의 자식이어야 한다.
            # 즉 이번에 처음 방문한 것이어야 한다. 그런데 만약 이전에 이미 방문한 적이 있다면 root를 루트 노드로 삼는 트리는 존재하지 않는다는 것을 의미한다.
            for child in adj_list[node]:
                if parent[node] == child:
                    continue
                # child를 이미 방문했기 때문에 더이상 트리가 될수 없다는 것을 알게 되어도 탐색은 멈추지 않는다.
                # root 노드와 연결된 모든 노드들을 전부 방문해야 그 다음 트리를 찾을때 방해가 되지 않기 떄문이다.
                if visited[child]:
                    is_tree = False
                if not visited[child]:
                    visited[child] = True
                    q.append(child)
                    parent[child] = node

        if is_tree:
            tree_count += 1

    print("Case " + str(tc), end='')
    if tree_count == 0:
        print(": No trees.")
    elif tree_count == 1:
        print(": There is one tree.")
    else:
        print(": A forest of " + str(tree_count) + " trees.")