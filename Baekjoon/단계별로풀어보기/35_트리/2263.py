# 걸린 시간 : 1시간 30분
# 제출 횟수 : 4번
# 풀이 참조 : x
# 반례 참조 : x

import sys

n = int(input())
in_order = list(map(int, sys.stdin.readline().split()))
post_order = list(map(int, sys.stdin.readline().split()))

# 이 문제에서는 노드의 번호가 중복되지 않기 때문에 각 노드에 해당되는 인덱스 정보를 맵에 저장해서 빠르게 인덱스를 찾는다.
in_index = dict()
post_index = dict()
for i in range(n):
    post_index[post_order[i]] = i
    in_index[in_order[i]] = i

# 밑에서는 스택을 이용해 구현하였지만, 재귀 제한을 풀고 재귀로 풀어도 된다.
answer = []
stack = []
# 노드 i의 왼쪽 노드를 방문했는지(스택에 넣었는지)를 체크한다.
left_visited = [False] * n

# 트리는 인오더든, 포스트 오더든, 프리 오더든, 왼쪽 서브트리를 전부 방문한 뒤에 루트노드나 오른쪽 서브트리를 방문할 수있다.
# 따라서 서브트리는 인오더와 포스트오더에서 모여있게 된다.
# 인오더에서 루트 노드의 인덱스를 i라고 하면, 0 ~ i-1의 인덱스는 전부 왼쪽 서브트리이고,
# i+1 ~ 끝 까지는 전부 오른쪽 서브트리가 된다.
# 또한 포스트오더에서는 해당 서브트리의 루트노드는 항상 맨 끝에 위치하게 된다.
# 즉 전체트리에서는 루트노드가 가장 마지막 인덱스에 있고,
# 이는 왼쪽 서브트리와 오른쪽 서브트리에 대해서도 똑같이 적용된다.
# 따라서 스택에 현재 방문하려는 서브트리의 왼쪽, 오른쪽 인덱스와(이는 인오더의 인덱스이다) 루트 노드의 인덱스(이는 포스트 오더의 인덱스이다)를 집어 넣으면서
# 그 서브트리의 왼쪽 서브트리를 전부 스택에 집어 넣고, 그 다음에 오른쪽 서브트리를 전부 스택에 집어넣는다.

# 스택에 전체 트리의 루트노드 인덱스인 n-1, 전체 트리의 왼쪽 오른쪽 인덱스를 스택에 집어넣는다.
stack.append([n-1, 0, n-1])
while stack:
    root_index, left_index, right_index = stack[-1]

    if left_index > right_index:
        stack.pop()
        continue
    # 만약 현재 방문하려는 서브트리가 노드 하나라면, 왼쪽 오른쪽 서브트리가 더이상 존재하지 않으므로 현재 노드를 anwer에 넣고 스택에서 팝 한다.
    if left_index == right_index:
        stack.pop()
        answer.append(in_order[left_index])
        continue

    root = post_order[root_index]
    # 현재 서브트리의 루트노드가 인오더에서 어떤 인덱스에 있는지를 i에 저장한다.
    i = in_index[root]

    # 만약 현재 서브트리의 왼쪽 서브트리를 아직 방문하지 않았다면 왼쪽 서브트리를 먼저 방문한다.
    # 왼쪽 서브트리를 전부 방문한 뒤에 오른쪽 서브트리를 방문해야 하기 때문에 현재 오른쪽 서브트리는 방문하지 않는다.
    # 하지만 이후에 방문해야 하기 때문에 현재 서브트리를 스택에서 팝 하지는 않는다.
    if not left_visited[i]:
        # 먼저 왼쪽 서브트리를 방문하기 전에 현재 서브트리의 루트노드를 answer에 집어넣는다.
        answer.append(in_order[i])
        # 왼쪽 서브트리를 방문하기 위해 스택에 집어넣는다.
        stack.append([root_index - (right_index - i + 1), left_index, i - 1])
        left_visited[i] = True

    # 만약 왼쪽 서브트리를 방문을 다 하고나면 이제 오른쪽 서브트리를 방문할 차례이다.
    # 현재 서브트리의 루트노드와 왼쪽 서브트리는 이미 방문했기 때문에 현재 서브트리는 더이상 방문할 필요가 없다.
    # 따라서 현재 서브트리가 스택에 맨 위에 저장되어 있기 때문에 팝한 뒤에 오른쪽 서브트리를 방문한다.
    # 이렇게 하는 대신 right_visited를 만들어서 왼쪽 오른쪽 서브트리를 전부 방문했다면 그때 스택에서 팝해도 된다.
    else:
        stack.pop()
        stack.append([root_index - 1, i + 1, right_index])

# 루트 -> 왼쪽 서브트리 -> 오른쪽 서브트리 순으로 방문한 프리 오더를 화면에 출력한다.
print(*answer)

'''
인오더 : left 서브트리 방문 후 루트 노드 방문 후 right 서브트리 방문
포스트오더 : left 서브트리 방문 후 right 서브트리 방문 후 루트 노드 방문
프리오더 : 루트 노드 먼저 방문 후 left -> right
포스트 오더에서 루트 노드는 가장 마지막에 존재한다.
이 루트노드를 기준으로 인오더에서는 왼쪽, 오른쪽이 나뉜다.
'''