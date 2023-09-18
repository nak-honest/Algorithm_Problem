# 걸린 시간 : 36분
# 제출 횟수 : 1번
# 풀이 참조 : x
import sys

def add(x, y):
    if x == sys.maxsize or y == sys.maxsize:
        return sys.maxsize
    else:
        return x + y

# 분할 정복으로 x -> y 경로를 구한다. 이때 가장 끝 경로 y는 추가되지 않는다.
def get_route(x, y, route_list):
    if len(route[x][y]) == 2:
        route_list.append(x)
        return

    get_route(x, route[x][y][1], route_list)
    get_route(route[x][y][1], y, route_list)


n = int(input())
m = int(input())

W = [[sys.maxsize] * (n+1) for _ in range(n+1)]

# route[i][j]는 i -> j 로 가는 최단 경로에 중간에 거쳐가는 노드가 있는지를 저장한다.
# route[i][j]가 비어있다면 경로가 없다는 것이고, [i, j]라면 i -> j 직행으로 가는게 최단 경로라는 것이다.
# route[i][j]가 [i, k, j]라면 i -> j를 갈때 k를 거쳐가야 최단경로가 된다는 것이다.
route = [[[] for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    W[a][b] = min(W[a][b], c)
    if not route[a][b]:
        route[a][b].extend([a, b])

for i in range(1, n+1):
    W[i][i] = 0


dp = W.copy()

# 플로이드 와샬 알고리즘 적용
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if add(dp[i][k], dp[k][j]) < dp[i][j]:
                dp[i][j] = add(dp[i][k], dp[k][j])
                # dp[i][j]가 업데이트 되었다면, 중간에 k를 거쳐가는 것이 최단 경로임을 의미한다.
                # 이를 업데이트 한다.
                # 길이가 0이라는 것은 i -> j로 가는 경로가 이전까지는 없었음을 의미한다.
                if len(route[i][j]) == 0:
                    route[i][j].extend([i, k, j])

                # 길이가 2라는 것은 i -> j 직행으로 가는 경로가 이전까지는 최단경로 였는데, 이제는 k를 거쳐가는 것이 최단 경로임을 의미한다.
                elif len(route[i][j]) == 2:
                    route[i][j].insert(1, k)

                # 이미 이전에 k가 추가되었는데, dp[i][j]가 업데이트 되었다는 것은 이전의 k가 아니라 현재 k를 거쳐가는 것이 더 빠르다는 것이다.
                # 따라서 업데이트 한다.
                else:
                    route[i][j][1] = k

# 먼저 최단 경로 비용을 출력한다.
for i in range(1, n+1):
    for j in range(1, n+1):
        if dp[i][j] == sys.maxsize:
            print(0, end='')
        else:
            print(dp[i][j], end='')

        if j == n:
            print()
        else:
            print(' ', end='')

# 그후 최단 경로의 도시 개수와 최단 경로를 출력한다.
for i in range(1, n+1):
    for j in range(1, n+1):
        if not route[i][j]:
            print(0)

        # 길이가 2라는 것은 i -> j 직행으로 가는 것이 최단경로임을 의미한다.
        elif len(route[i][j]) == 2:
            print(*[2, i, j])
        # 길이가 3이라는 것은 i -> k -> j 로 가는 것이 최단 경로임을 의미하는데,
        # i -> k로 가는 최단경로와 k -> j로 가는 최단 경로도 구해야 한다.
        # 이는 분할 정복을 이용해서 구할수 있다.
        else:
            answer = []
            get_route(i, j, answer)
            answer.append(j)
            print(len(answer), *answer, sep=' ')
