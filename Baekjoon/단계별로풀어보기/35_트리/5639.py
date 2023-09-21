# 걸린 시간 : 1시간 30분
# 제출 횟수 : 7번
# 풀이 참조 : x
# 반례 참조 : x

stack = []

# 후위 순회를 돌며 출력한다.
def reverse_order(r):
    visited = [False] * len(nodes)
    stack.append(r)

    while stack:
        node = stack[-1]
        if left[node] != -1 and not visited[left[node]]:
            stack.append(left[node])
        elif right[node] != -1 and not visited[right[node]]:
            stack.append(right[node])
        else:
            print(nodes[node])
            stack.pop()
            visited[node] = True

nodes = list(map(int, open(0).read().split()))

root = 0
left = [-1] * len(nodes)
right = [-1] * len(nodes)
parent = [-1] * len(nodes)

prev = 0

# 전위 순회를 따라 각 노드의 왼쪽 자식, 오른쪽 자식, 부모 노드 정보를 업데이트 한다.
for i in range(1, len(nodes)):
    # 왼쪽 노드는 먼저 방문하기 때문에, 현재 노드가 이전 노드보다 크다면 바로 왼쪽 자식 노드임을 의미한다.
    if nodes[prev] > nodes[i]:
        left[prev] = i
        parent[i] = prev

    # 이전 노드보다 크다면, 이전 노드 뿐만 아니라 이전 노드의 부모도 살펴보아야 한다.
    # 현재 노드가 이전 노드의 부모노드보다 큰데, 이전 노드가 부모노드의 왼쪽 자식이라면 이전 노드의 오른쪽에 놓으면 안된다.
    # 따라서 현재 노드를 어디에 놓아야 하는지를 부모 노드들 까지 포함해서 찾는다.
    else:
        while parent[prev] != -1 and nodes[parent[prev]] < nodes[i]:
            prev = parent[prev]

        while right[prev] != -1:
            prev = right[prev]

        right[prev] = i
        parent[i] = prev

    prev = i

reverse_order(root)