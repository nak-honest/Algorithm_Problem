# 걸린 시간 : 23분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

import sys

def find_root(i):
    while i != union[i]:
        i = union[i]

    return i


for _ in range(int(input())):
    F = int(input())

    user_to_index = dict()
    index = 0

    # 친구 정보를 업데이트 할때마다 union find를 업데이트 한다.
    union = []
    depth = []

    # 루트 노드의 인덱스를 root라 하면 count[root]에는 해당 union find의 원소 개수가 저장된다.
    count = []

    for _ in range(F):
        u, v = sys.stdin.readline().split()

        # 먼저 처음 나오는 사람의 이름이 있다면, 해당 사람에 대한 인덱스 정보를 업데이트한다.
        # 그와 함께 관련된 리스트들도 전부 업데이트 한다.
        if u not in user_to_index:
            user_to_index[u] = index
            union.append(index)
            depth.append(0)
            count.append(1)
            index += 1
        if v not in user_to_index:
            user_to_index[v] = index
            union.append(index)
            depth.append(0)
            count.append(1)
            index += 1

        # 각 사람에 대한 인덱스를 얻는다.
        u_index = user_to_index[u]
        v_index = user_to_index[v]

        # 각 노드가 속해있는 union find의 루트 노드를 찾는다.
        root_u = find_root(u_index)
        root_v = find_root(v_index)

        # u와 v가 속해있는 union find가 합쳐질텐데, 합쳐진 union find의 루트노드를 저장한다.
        root = root_u

        # 서로 다른 union find에 있다면, 두 union find를 합친다.
        # 이때 depth가 늘지 않을 수 있다면 늘지 않도록 합친다.
        if root_u != root_v:
            if depth[root_u] > depth[root_v]:
                union[root_v] = root_u
                count[root_u] += count[root_v]
            elif depth[root_u] < depth[root_v]:
                union[root_u] = root_v
                count[root_v] += count[root_u]
                root = root_v
            else:
                union[root_v] = root_u
                count[root_u] += count[root_v]
                depth[root_u] += 1

        # 합쳐진 union find의 원소 개수를 출력한다.
        print(count[root])
