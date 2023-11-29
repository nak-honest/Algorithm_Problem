import sys

N, M, B = map(int, input().split())

# 각 높이를 하나하나 세지 않고, 한번에 셀수 있도록 높이의 개수를 저장한다.
height_count = [0] * 257
for _ in range(N):
    for h in map(int, sys.stdin.readline().split()):
        height_count[h] += 1

# 높이 h로 만들려고 할때 필요한 시간을 hegiht_cost[h]에 저장한다.
answer_h = 0
answer_cost = sys.maxsize

# 각 높이를 만드는데 필요한 시간을 계산한다.
for target_h in range(257):
    remove_count = 0
    add_count = 0
    for h in range(target_h):
        add_count += height_count[h] * (target_h - h)
    for h in range(target_h + 1, 257):
        remove_count += height_count[h] * (h - target_h)

    if add_count > remove_count + B:
        continue

    cur_cost = remove_count * 2 + add_count

    # 정답보다 시간이 적게 들거나 같은 경우, 정답을 업데이트 한다. (비용이 같다면 높이가 높은 게 정답이므로)
    if cur_cost <= answer_cost:
        answer_h = target_h
        answer_cost = cur_cost

print(answer_cost, answer_h, sep=' ')