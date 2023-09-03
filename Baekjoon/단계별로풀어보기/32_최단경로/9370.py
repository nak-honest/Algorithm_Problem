import sys
from heapq import heappop, heappush


def add_dest(i, j):
    if i == sys.maxsize or j == sys.maxsize:
        return sys.maxsize
    return i + j


def dijkstra(adj, start):
    heap = []
    cur_dest = [sys.maxsize] * (n + 1)
    visited = [False] * (n + 1)

    cur_dest[start] = 0
    heap.append((0, start))

    while heap:
        dest, node = heappop(heap)

        if visited[node]:
            continue

        visited[node] = True

        for next_dest, next in adj[node]:
            if not visited[next] and dest + next_dest < cur_dest[next]:
                cur_dest[next] = dest + next_dest

                heappush(heap, (cur_dest[next], next))

    return cur_dest


for _ in range(int(input())):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    adj_list = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        adj_list[a].append((d, b))
        adj_list[b].append((d, a))

    candidates = [int(input()) for _ in range(t)]

    # s -> 목적지 후보 로 가는 최단 경로와 min(s -> g -> h -> 목적지 후보, s -> h -> g -> 목적지 후보) 가 같다면,
    # g-h 교차로를 지나서 최단 경로를 만들수 있다는 것을 의미한다.
    # 따라서 s, g, h를 출발지로 해서 각 노드로 가는 최단 경로를 다익스트라로 구한다.
    dest_from_s = dijkstra(adj_list, s)

    dest_to_g = dest_from_s[g]
    dest_to_h = dest_from_s[h]

    dest_from_g = dijkstra(adj_list, g)
    dest_from_h = dijkstra(adj_list, h)

    dest_between_g_h = sys.maxsize

    for dest, node in adj_list[g]:
        if node == h:
            dest_between_g_h = dest
            break


    answer = []

    for candidate in sorted(candidates):
        # s -> candidate 로 가는 실제 최단 경로
        dest_to_candidate = dest_from_s[candidate]

        # s -> g -> h -> candidate 로 가는 최단 경로
        dest1 = add_dest(add_dest(dest_to_g, dest_between_g_h), dest_from_h[candidate])
        # s -> h -> g -> candidate 로 가는 최단 경로
        dest2 = add_dest(add_dest(dest_to_h, dest_between_g_h), dest_from_g[candidate])

        if dest_to_candidate != sys.maxsize and dest_to_candidate == min(dest1, dest2):
            answer.append(candidate)


    print(*answer)
