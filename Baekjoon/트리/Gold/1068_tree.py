import sys
from collections import deque

N = int(input())

# 노드 i의 부모노드 번호를 저장한다.
parent = list(map(int, sys.stdin.readline().split()))

# 노드 i를 루트로 하는 서브트리의 리프노드 개수를 저장한다.
# 부모 노드는 자식 노드가 가지고 있는 리프노드 개수의 합과 같다.
leaf_num = [0 for _ in range(N)]

# 부모 노드는 자식노드가 가지고 있는 리프노드 개수만큼 자신의 리프노드 개수에 더해야한다.
# 하지만 자식노드의 리프노드 개수가 아직 다 더해지지 않았다면 부모노드에 더할 수 없다. -> 중복되어서 더해지기 때문!
# 따라서 각 노드마다 자식의 리프노드 개수를 더했는지 체크하기 위해 아직 더하지 않은 자식을 이중 리스트로 저장한다.
# to_add_child[i]는 노드 i의 자식중 아직 리프노드 개수를 합산하지 않은 자식 리스트이다.
to_add_child = [[] for _ in range(N)]

# 자식이 없는 노드, 즉 리프노드의 인덱스를 저장한다.
no_child = {i: 0 for i in range(N)}

# 리프 노드의 개수를 구한 노드들을 넣는 곳이다.
# low_index에 있는 노드를 꺼내서 부모노드의 리프노드 개수에 더한다.
low_index = deque()

# 루트 노드가 0번이 아닐수 있다고 생각하여 따로 구한다.
root_index = 0

# 각 노드의 자식 노드 개수를 저장한다.
child_num = [0 for _ in range(N)]

# parent[i] 정보를 통해 to_add_child, child_num 을 업데이트 한다.
for i in range(N):
    # 부모가 없다면, 노드 i는 루트노드이다.
    if parent[i] == -1:
        root_index = i
        continue

    to_add_child[parent[i]].append(i)
    child_num[parent[i]] += 1

    # no_child에서 부모 노드를 삭제한다.
    if parent[i] in no_child:
        del no_child[parent[i]]

# 먼저 리프노드의 리프노드 개수를 1로 설정하고, low_index에 넣는다.
for i in no_child:
    leaf_num[i] = 1
    if parent[i] != -1:
        low_index.append(i)

# low_index가 빌 때까지 부모노드의 리프노드 개수를 업데이트 한다.
# low_index는 계속해서 업데이트 된다.
while len(low_index) > 0:
    cur_len = len(low_index)
    for _ in range(cur_len):
        i = low_index.popleft()

        # i가 루트노드가 아니고, 노드 i가 리프 노드 계산이 끝난 경우 노드 i의 부모노드 리프노드 개수에 더한다.
        if parent[i] != -1 and not to_add_child[i]:
            leaf_num[parent[i]] += leaf_num[i]
            to_add_child[parent[i]].remove(i)

            # 노드 i의 부모가 루트노드가 아니고, 리프노드 계산이 끝난 경우에만 low_index에 넣는다.
            if parent[i] != root_index and not to_add_child[parent[i]]:
                low_index.append(parent[i])
        # 노드 i가 아직 리프노드 계산이 끝나지 않은 경우 low_index에 넣는다.
        elif parent[i] != -1:
            low_index.append(i)

del_index = int(input())

# 전체 트리의 리프노드 개수에서 지우고자 하는 노드의 리프노드 개수를 빼면 남은 리프노드의 개수가 된다.
answer = leaf_num[root_index] - leaf_num[del_index]

# 이때 만약 지운 노드가 부모 노드의 유일한 자식이었다면, 해당 노드를 지울때 부모노드가 리프노드가 되어 전체 리프노드는 1개 증가하게 된다.
# 이를 반영하기 위해 개수를 1 증가시킨다.
if child_num[parent[del_index]] == 1:
    answer += 1

print(answer)
