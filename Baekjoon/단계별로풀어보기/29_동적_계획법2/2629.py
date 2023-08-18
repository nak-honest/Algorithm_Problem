# 추의 개수가 얼마 안되어서 그냥 만들수 있는 모든 구슬의 무게를 구하였다.
# 냅색과 비슷하게 푼 dp를 이용한 풀이를 보니 로직 자체는 큰 차이가 없는 것 같다.

import sys
from bisect import bisect_left, insort_left

weights_num = int(input())
weights = list(map(int, sys.stdin.readline().split()))
marbles_num = int(input())
marbles = list(map(int, sys.stdin.readline().split()))

# 측정할 수 있는 구슬 무게의 후보
marbles_candidate = [0]

# 추를 하나씩 가지고 와서 새로 측정 가능한 구슬 무게의 후보를 업데이트 한다.
for w in weights:
    # candidate 무게의 구슬을 측정할 수 있을때 w라는 추가 하나 추가된다면, 새로 측정할 수 있는 구슬 무게는 다음과 같다.
    # 먼저 더 무거운 쪽의 추의 무게가 x라고 한다면 가벼운 쪽은 x - candidate의 추가 올려져 있게 된다. 그래야 양쪽의 무게 차가 candidate가 되기 때문!
    # 이때 더 무거운 쪽에 w 무게의 추를 올린다면 양쪽의 무게 차는 w + candidate 가 되므로 w + candidate 라는 무게의 구슬을 측정할 수 있게 된다.
    # 반대로 더 가벼운 쪽에 w 무게의 추를 올린다면 양쪽의 무게 차는 abs(w - candidate) 가 되므로
    # abs(w - candidate) 라는 무게의 구슬을 측정할 수 있게 된다.
    for candidate in marbles_candidate[:]:
        new_candidate1 = candidate + w
        new_candidate2 = abs(candidate - w)

        index1 = bisect_left(marbles_candidate, new_candidate1)

        if index1 == len(marbles_candidate) or marbles_candidate[index1] != new_candidate1:
            insort_left(marbles_candidate, new_candidate1)

        index2 = bisect_left(marbles_candidate, new_candidate2)

        if index2 == len(marbles_candidate) or marbles_candidate[index2] != new_candidate2:
            insort_left(marbles_candidate, new_candidate2)

# 각 구슬이 측정 가능하다면 marbles_candidate에 들어있으므로, 이를 보고 정답을 출력한다.
for marble in marbles:
    index = bisect_left(marbles_candidate, marble)
    if index < len(marbles_candidate) and marbles_candidate[index] == marble:
        print("Y", end=' ')
    else:
        print("N", end=' ')