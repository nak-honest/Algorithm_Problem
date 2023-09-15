# 역시 dp.. 정말 어려웠따 ㅠㅠ 최근에 좀 잘 풀려서 실력이 늘었구나 생각했지만 역시 사람은 겸손해야 한다.

# 처음에는 매 사건 지점을 1이 갈때의 최단 경로, 2가 갈때의 최단 경로를 dp에 각각 저장해서 풀었다.
# 다음 사건이 발생하면 1 -> 1, 2 -> 1 중 최단을 저장, 1 -> 2, 2 -> 2 중 최단을 저장하였다.
# 하지만 이렇게 풀면 두 경찰차로부터 같은 거리에 있는 사건인 경우에 어떤 경찰차를 선택해야 하는지 결정할 기준이 없는 것이 문제였다.
# 따라서 거리가 같은 경우에 각 경찰차를 고정으로 삼았을 떄의 경우도 생각하여서 풀려했지만 끝내 풀지 못하였다.

# 그 후 인터넷을 참고하여 dp[i][j] 는 1번이 마지막 도착한 곳이 i이고 2번이 마지막 도착한곳이 j일 때의 최단 경로를 저장한다는 사실만 확인해서 풀었다.
# 해당 아이디어를 떠올리는 것 자체는 결국 해내지 못했지만, 어떻게 점화식을 세우고, 경로 추적은 어떻게 하는지는 직접 구현하였다.

import sys

def get_len(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

N = int(input())
W = int(input())

# event[i] 는 i번쨰 사건의 위치를 저장한다.
event = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(W)]

# dp[i][j][0]에는 1번 경찰차가 마지막으로 도착한 곳이 i이고, 2번 경찰차가 마지막으로 도착한 곳이 j일때의 최단 경로를 저장한다.
# 그리고 dp[i][j][1]에는 그렇게 최단 경로를 만들도록 하려면 몇번 경찰차가 이동해야하는지를 저장한다.
# 또한 dp[i][j]에서 1번 경찰차의 위치가 i번째 사건의 위치이고, 2번 경찰차의 위치가 j번째 사건의 위치임을 알수 있다.
# 왜냐하면 마지막 처리한 사건의 위치에 대기하기 때문이다.
dp = [[[sys.maxsize, -1] for _ in range(W+1)] for _ in range(W+1)]

# prev[i][j]에는 역추적을 위해 dp[i][j]를 만들도록 하는 이전 dp의 인덱스를 저장한다. -> 그 dp에 몇번 경찰차가 이동했는지 저장되어 있기 때문이다.
prev = [[[-1, -1] for _ in range(W+1)] for _ in range(W+1)]

# dp[1][0][0]의 의미는 1번 경찰차가 1번 사건에 있고, 2번 경찰차가 가만히 있을때의 최단 경로를 의미한다.
dp[1][0][0] = get_len((1, 1), event[1])
# 1번 경찰차가 사건으로 이동했음을 의미한다.
dp[1][0][1] = 1

# 2번 경찰차가 계속해서 가만히 있고 1번 혼자서 모든 사건을 처리하는 경우의 최단경로를 모두 업데이트한다.
for i in range(2, W+1):
    dp[i][0][0] = dp[i-1][0][0] + get_len(event[i-1], event[i])
    dp[i][0][1] = 1
    prev[i][0] = [i-1, 0]


# 반대로 1번 경찰차가 계속해서 가만히 있고 2번 혼자서 모든 사건을 처리하는 경우의 최단 경로를 모두 업데이트한다.

dp[0][1][0] = get_len((N, N), event[1])
dp[0][1][1] = 2

for j in range(2, W+1):
    dp[0][j][0] = dp[0][j-1][0] + get_len(event[j-1], event[j])
    dp[0][j][1] = 2
    prev[0][j] = [0, j-1]


# for문을 돌며 dp[i][j]와 prev[i][j]를 업데이트 한다.
for i in range(1, W+1):
    for j in range(1, W+1):
        # 먼저 i와 j가 같을 수는 없다. i와 j가 같다는 것은 1번, 2번 경찰차 모두 같은 사건을 처리한다는 의미이다.
        if i == j:
            continue

        # dp[i][j]를 업데이트 해야하는데 j-1 > i 인 경우, 현재 처리해야 하는 사건이 j번째 사건이라는 것을 의미한다.
        # 그런데 j-1 이 i보다 크다면 j-1번째 사건을 2번째 경찰차가 처리했다는 것을 의미하게 된다.
        # 왜냐하면 dp[i][x]의 의미는 1번 경찰차가 마지막으로 처리한 사건이 i번째 사건이라는 의미이기 떄문이다.
        if j-1 > i:
            dp[i][j][0] = dp[i][j-1][0] + get_len(event[j-1], event[j])
            dp[i][j][1] = 2
            prev[i][j] = [i, j-1]

        # 이번에는 반대로 i-1 > j 라는 것은 현재 처리해야 하는 사건이 i번째 사건이라는 것을 의미하고,
        # i-1번째 사건을 1번 경찰차가 처리했다는 것을 의미한다.
        elif i-1 > j:
            dp[i][j][0] = dp[i-1][j][0] + get_len(event[i-1], event[i])
            dp[i][j][1] = 1
            prev[i][j] = [i-1, j]

        # j > i 이기 때문에 이번에 처리해야 하는 사건이 j번째 사건임을 의미한다.
        # 하지만 i가 j-1이기 때문에 j-1번째 사건은 1번 경찰차가 처리했다는 것을 의미한다. 즉 2번 경찰차는 j-1번째 사건을 처리할 수 없다.
        # j-1번째 사건은 1번 경찰차가 해결했으므로 2번 경찰차는 이전에 아예 사건처리를 안했거나 1~j-2 번째 사건을 마지막으로 처리했음을 알수 있다.
        # 따라서 1번 경찰차가 j-1번째를 마지막으로 처리한 상황에서 2번 경찰차가 마지막으로 처리한 사건이 무엇이냐에 따라 dp[i][j][0]의 값은 바뀔 것이다.
        # 이중 최소값을 dp[i][j][0]에 저장하면 된다.
        elif i == j-1:
            min_len = sys.maxsize
            min_j = 0

            # 2번 경찰차가 이전에 아무 사건도 처리하지 않다가 이번에 처음으로 j번째 사건을 처리하는 경우이다.
            if min_len > dp[i][0][0] + get_len((N, N), event[j]):
                min_len = dp[i][0][0] + get_len((N, N), event[j])
                min_j = 0

            # 2번 경찰차가 이전에 마지막으로 처리한 사건이 k번째 사건이고, 이번에 j번째 사건을 처리하는 경우이다.(1 <= k <= j-2)
            for k in range(1, j-1):
                if min_len > dp[i][k][0] + get_len(event[k], event[j]):
                    min_len = dp[i][k][0] + get_len(event[k], event[j])
                    min_j = k

            # 이중 최솟값을 저장한다.
            dp[i][j][0] = min_len
            dp[i][j][1] = 2

            prev[i][j] = [i, min_j]

        # 마지막은 j == i-1인 경우이다. 이는 현재 처리해야 하는 사건이 i번째 사건임을 의미한다.
        # 위의 상황과 마찬가지로 j가 i-1이므로 2번 경찰차가 마지막으로 i-1번째 사건을 처리했다.
        # 따라서 똑같이 1번 경찰차가 이전에 사건처리를 아예 안했거나 1~i-2 번째 사건을 마지막으로 처리한 경우를 모두 확인해서 그중 최솟값을 저장한다.
        else:
            min_len = sys.maxsize
            min_i = 0

            # 1번 경찰차가 이전에 아무 사건도 처리하지 않다가 이번에 처음으로 i번째 사건을 처리하는 경우이다.
            if min_len > dp[0][j][0] + get_len((1, 1), event[i]):
                min_len = dp[0][j][0] + get_len((1, 1), event[i])
                min_i = 0

            # 1번 경찰차가 이전에 마지막으로 처리한 사건이 k번째 사건이고, 이번에 i번째 사건을 처리하는 경우이다.(1 <= k <= i-2)
            for k in range(1, i-1):
                if min_len > dp[k][j][0] + get_len(event[k], event[i]):
                    min_len = dp[k][j][0] + get_len(event[k], event[i])
                    min_i = k

            # 이중 최솟값을 저장한다.
            dp[i][j][0] = min_len
            dp[i][j][1] = 1

            prev[i][j] = [min_i, j]

# 먼저 정답인 최단 경로를 찾는다.
# 최단 경로는 1번 경찰차나 2번 경찰차중 하나가 W에 도달한 경로중 최솟값이 된다.
min_len = sys.maxsize
cur_i = 0
cur_j = 0

# 2번 경찰차가 W에 도달한 경우
for i in range(W):
    if dp[i][W][0] < min_len:
        min_len = dp[i][W][0]
        cur_i = i
        cur_j = W

# 1번 경찰차가 W에 도달한 경우
for j in range(W):
    if dp[W][j][0] < min_len:
        min_len = dp[W][j][0]
        cur_i = W
        cur_j = j

print(min_len)

# answer에는 경로를 역순으로 저장한다.
answer = []

# cur_i와 cur_j 중 큰 값을 cur이라 하면(cur = max(cur_i, cur_j))
# cur번째 사건을 처리한 경찰차는 dp[cur_i][cur_j][1]에 저장되어 있다.
# 그리고 그 이전 사건을 처리한 dp의 인덱스는 prev[cur_i][cur_j]에 저장되어 있다. 이를 이용하여 최단 경로를 추적한다.
while not (cur_i == -1 and cur_j == -1):
    answer.append(dp[cur_i][cur_j][1])
    cur_i, cur_j = prev[cur_i][cur_j]

print(*reversed(answer), sep='\n')
