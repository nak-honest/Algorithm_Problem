from collections import deque


# node를 2씩 곱한 노드를 방문한다.
def visit_all_power_of_two(next, count):
    while next * 2 <= V:
        next *= 2

        # 만약 node를 2씩 곱한 노드를 이전에 방문했다면, 그 노드의 2씩 곱한 모든 노드들도 방문한 것이므로 while문을 탈출한다.
        # 하지만 그러기 위해서는 node-1, node+1 을 방문할때 즉시 2씩 곱한 모든 노드들을 방문해야 한다.
        if visited[next]:
            return

        q.append((next, count))
        visited[next] = True


N, K = map(int, input().split())
V = 100_000

visited = [False] * (V+1)
q = deque()

visited[N] = True
q.append((N, 0))

# bfs를 돌며 count를 1씩 증가시키며 최단경로를 찾는다.
while q:
    node, count = q.popleft()

    if node == K:
        print(count)
        break

    # 먼저 node를 2씩 곱한 노드를 방문한다.
    visit_all_power_of_two(node, count)

    if node-1 >= 0 and not visited[node-1]:
        q.append((node-1, count+1))
        visited[node-1] = True

        # node-1을 방문하면, 그 즉시 node-1를 2씩 곱한 노드를 방문한다.
        visit_all_power_of_two(node-1, count+1)

    if node+1 <= V and not visited[node+1]:
        q.append((node+1, count+1))
        visited[node+1] = True

        # node+1을 방문하면, 그 즉시 node+1를 2씩 곱한 노드를 방문한다.
        visit_all_power_of_two(node+1, count+1)
