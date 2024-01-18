# pypy3로 전체 13등을 했다. 하지만 좀 복잡하게 푼것 같다..

# 걸린 시간 : 1시간 40분
# 제출 횟수 : 10번
# 풀이 참조 : x
# 반례 참조 : x

import sys
from heapq import heapify
from heapq import heappop

N, K = map(int, input().split())
jewels = []
C = []

# 이거 때문에 좀 효율적으로 돌아간다.
# right_index[i]는 C[i] 가방이 이미 보석을 담고 있다면, 그 다음에 어떤 가방에 넣어야 할지 그 가방의 인덱스를 저장한다.
right_index = list(range(K))

# 보석들을 가치가 높은 순으로, 가치가 같다면 무게가 낮은 순으로 pop하는 heap으로 구성한다.
for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    jewels.append((-V, M))

for _ in range(K):
    C.append(int(sys.stdin.readline()))

# 가방의 무게를 정렬한다.
C.sort()
heapify(jewels)
answer = 0

# 보석을 하나씩 pop한다.
while jewels and right_index[0] != -1:
    v, m = heappop(jewels)
    v = -v

    # 보석의 무게보다 큰 가방 중, 가장 무게가 낮은 가방을 찾는다.
    index = K-1
    if C[index] < m:
        continue

    # 이분탐색으로 찾는다.
    K_diff = K // 2
    while K_diff > 0 and index - K_diff >= 0:
        if C[index] == m:
            break
        if C[index - K_diff] > m:
            index -= K_diff

        K_diff //= 2

    while index > 0 and C[index-1] >= m:
        index -= 1

    # right_index가 업데이트 되어야 하는 index들을 모아놓는다.
    # 매번 업데이트 하지 않으면, 느리기 때문에 차라리 안쓰는게 낫다.
    indices = [index]

    # 아직 C[index] 가방에 보석을 담지 않은 경우
    if right_index[index] == index:
        answer += v

        # 가장 무게가 무거운 가방에 보석을 담은 경우에는 더이상 다음 가방이 존재하지 않는다.
        # 이 경우에는 right_index의 값을 -1로 설정한다.
        if index == K-1:
            right_index[index] = -1
        else:
            # C[index] 가방에 보석을 채웠기 때문에, 그 다음에는 보석을 어느 가방에 넣어야 할지 찾는다.
            next_index = index + 1
            while next_index != -1 and next_index != right_index[next_index]:
                indices.append(next_index)
                next_index = right_index[next_index]

            # right_index를 모두 업데이트 한다.
            for i in indices:
                right_index[i] = next_index

    # C[index] 가방에 보석을 이미 담은 경우
    elif right_index[index] != -1:
        # 어느 가방에 보석을 넣어야 할지 인덱스를 찾는다.
        next_index = right_index[index]
        while next_index != -1 and next_index != right_index[next_index]:
            indices.append(next_index)
            next_index = right_index[next_index]

        # 다음 가방의 인덱스가 존재한다면 해당 가방에 보석을 담는다.
        if next_index != -1:
            answer += v
            indices.append(next_index)

            # C[next_index]가 가장 무거운 가방인데, 방금 보석을 채운 경우 더이상 다음 가방이 존재하지 않는다.
            if next_index == K-1:
                for i in indices:
                    right_index[i] = -1
            # C[next_index] 가방에 보석을 채웠기 때문에, 그 다음에는 보석을 어느 가방에 넣어야 할지 찾는다.
            else:
                next_next_index = next_index + 1
                while next_next_index != -1 and right_index[next_next_index] != next_next_index:
                    indices.append(next_next_index)
                    next_next_index = right_index[next_next_index]

                # right_index를 모두 찾는다.
                for i in indices:
                    right_index[i] = next_next_index

        # 다음 가방의 인덱스가 존재하지 않는다면, 모두 right_index의 값을 -1로 업데이트 한다.
        else:
            for i in indices:
                right_index[i] = next_index

print(answer)
