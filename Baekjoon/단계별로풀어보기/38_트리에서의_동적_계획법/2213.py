# 걸린 시간 : 1시간
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

'''
      1
      2
    3   6
    4   7
    5

맨 밑 depth부터 1씩 올라간다.
올라가면서 해당 노드를 루트노드로 하는 서브트리의 최대 독립집합 크기를 dp에 저장한다.
-> max(자기 자신 + 자기 자식의 자식들의 dp 합, 자식들의 dp 합)
'''

from collections import deque
import sys

n = int(input())
w = [0] + list(map(int, sys.stdin.readline().split()))  # 가중치
parent = [-1] * (n + 1)  # 각 노드의 부모
children = [[] for _ in range(n + 1)]  # 각 노드의 자식들
adj_list = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

# 1번 노드를 루트 노드로 삼는다.
root = 1
q = deque()
q.append(root)
depth = [-1] * (n + 1)
depth[root] = 0

# 각 노드의 자식, 부모 노드와 depth를 구한다.
while q:
    p = q.popleft()
    for c in adj_list[p]:
        if c != parent[p]:
            parent[c] = p
            children[p].append(c)
            q.append(c)
            depth[c] = depth[p] + 1

# 같은 depth의 노드를 모은다.
depth_nodes = [[] for _ in range(max(depth) + 1)]

for i in range(1, n + 1):
    depth_nodes[depth[i]].append(i)

dp = [0] * (n + 1)

# dp에서 선택한 노드들을 역추적하기 위해, 이전에 어떤 노드들을 선택했는지 prev_nodes에 저장한다.
# 즉 자기 자식들의 dp 합을 선택했는지, 아니면 자기 자식들의 자식들의 dp 합을 선택했는지를 저장한다.
prev_nodes = [[] for _ in range(n + 1)]

# node를 루트노드로 하는 서브트리의 최대 독립집합 크기가 dp[node]인데, 이때 w[node]가 dp[node]에 포함되어 있는지를 저장한다.
# 즉 dp[node]의 값을 구할때, 해당 서브트리의 루트 노드를 포함하는지를 저장한다. 그래야 최대 독립 집합의 노드들을 구할 수 있다.
is_dp_contain_root = [False] * (n + 1)

# 가장 depth가 깊은 노드들부터 차례대로 dp값을 구한다.
for nodes in reversed(depth_nodes):
    for node in nodes:
        children_dp_sum = 0
        for c in children[node]:
            children_dp_sum += dp[c]

        children_of_children_dp_sum = 0
        for c in children[node]:
            for c_of_c in children[c]:
                children_of_children_dp_sum += dp[c_of_c]

        # 자기 자신 + 자기 자식의 자식들의 dp 합이 더 큰 경우
        if w[node] + children_of_children_dp_sum >= children_dp_sum:
            dp[node] = w[node] + children_of_children_dp_sum
            # dp[node]를 구할때 w[node] 값이 포함된다.
            is_dp_contain_root[node] = True

            # prev_nodes를 업데이트한다.
            for c in children[node]:
                prev_nodes[node].extend(children[c])
        else:
            dp[node] = children_dp_sum
            # prev_nodes를 업데이트한다.
            prev_nodes[node].extend(children[node])

max_sum = 0
max_root_node = -1
for i in range(1, n+1):
    if dp[i] > max_sum:
        max_sum = dp[i]
        max_root_node = i

# dp[max_root_node]를 구하기 위해 이전에 어떤 dp 값들을 더했는지 dp_set에 저장한다.
# 이때 dp_set에 있는 노드들이 실제 최대 독립 집합의 노드가 아니라는 것에 주의하자.
# dp[node]를 선택해도, 실제로는 해당 서브트리의 루트노드인 node는 포함이 안될 수 있기 때문이다.
dp_set = set()
q = deque()
q.append(max_root_node)

# 선택한 dp들을 모두 구한다.
while q:
    node = q.popleft()
    if node in dp_set:
        continue
    dp_set.add(node)

    for prev_node in prev_nodes[node]:
        q.append(prev_node)

# 선택한 dp 중 실제로 포함된 노드들만 구한다.
answer_nodes = list(filter(lambda x: is_dp_contain_root[x], dp_set))

print(max_sum)
print(*sorted(answer_nodes))
