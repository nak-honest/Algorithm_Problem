# 1654 문제와 거의 동일하다.
# 다만 여기에서는 누적합을 이용해 얻을 수 있는 나무의 길이를 빠르게 계산한다.


import sys
from bisect import bisect_left

N, M = map(int, input().split())
trees = sorted(list(map(int, sys.stdin.readline().split())))

# 뒤에서부터 누적합 저장
prefix_sum = trees[:]

for i in range(-2, -N-1, -1):
    prefix_sum[i] += prefix_sum[i+1]

h_diff = 1_000_000_000 // 2
cur_h = h_diff
answer = 0

while h_diff >= 1:
    total_len = 0
    index = bisect_left(trees, cur_h)

    # 만약 cur_h가 존재한다면 cur_h의 왼쪽 인덱스를 반환하기 때문에 1만큼 증가시켜 주어야 한다.
    if index < N and trees[index] < cur_h:
        index += 1

    # 누적합을 이용해 얻을수 있는 나무의 길이를 빠르게 구한다.
    if index < N:
        total_len = prefix_sum[index] - (cur_h * (N-index))

    h_diff //= 2

    if total_len >= M:
        answer = cur_h
        cur_h += h_diff
    elif total_len < M:
        cur_h -= h_diff


index = bisect_left(trees, answer)

while True:
    total_len = 0
    answer += 1

    # 만약 cur_h가 존재한다면 cur_h의 왼쪽 인덱스를 반환하기 때문에 1만큼 증가시켜 주어야 한다.
    index = bisect_left(trees, answer, index)
    if index < N and trees[index] < answer:
        index += 1

    if index < N:
        total_len = prefix_sum[index] - (answer * (N-index))

    if total_len < M:
        answer -= 1
        break

print(answer)