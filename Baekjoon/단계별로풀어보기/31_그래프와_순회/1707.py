import sys
from collections import deque

def bfs(adj):
    set1 = set()
    set2 = set()

    q = deque()
    visited = [False] * len(adj)

    q.append(1)
    visited[1] = True
    set1.add(1)

    while True:
        while q:
            node = q.popleft()

            for next in adj_list[node]:
                # bfs를 돌며 인접 노드를 방문하지 않았다면, 반대편 집합에 넣는다.
                if not visited[next]:
                    if node in set1:
                        set2.add(next)
                    else:
                        set1.add(next)
                    q.append(next)
                    visited[next] = True
                # 만약 인접 노드를 이전에 방문했다면, 같은 집합에 있는지 체크한다.
                elif (node in set1 and next in set1) or (node in set2 and next in set2):
                    return "NO"

        # bfs가 종료된 후에 아직 방문이 안된 노드가 있다면 그 노드를 시작으로 다시 bfs를 돌린다.
        for node in range(1, len(adj)):
            if not visited[node]:
                q.append(node)
                visited[node] = True
                set1.add(node)
                break
        if not q:
            return "YES"


for _ in range(int(input())):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    print(bfs(adj_list))


