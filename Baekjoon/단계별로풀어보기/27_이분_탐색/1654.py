import sys
from bisect import bisect_left

max_len = (pow(2, 31) - 1) // 2

K, N = map(int, input().split())
wires = sorted([int(sys.stdin.readline()) for _ in range(K)])

cur_len = max_len
answer = 0

# max_len을 2씩 나누면서 cur_len에 더하거나 뺀다.
# cur_len으로 N개의 랜선을 만들 수 없다면 cur_len에서 max_len을 빼고,
# cur_len으로 N개의 랜선을 만들 수 있다면 cur_len에서 max_len을 더한다.
# 이렇게 해서 최대한 정답에 가까운 값을 찾는다.
while max_len >= 1:
    wires_num = 0 # cur_len으로 만들 수 있는 랜선의 최대 개수를 저장한다.

    # cur_len으로 만들 수 있는 랜선의 최대 개수를 구한다.
    index = bisect_left(wires, cur_len)
    if index < K:
        for wire in wires[index:]:
            wires_num += wire // cur_len

    max_len //= 2

    # cur_len으로 N개보다 많은 랜선을 만들 수 있다면 cur_len에서 max_len // 2 를 더한다. (즉 cur_len을 오른쪽 영역의 가운데 값으로 설정한다.)
    if wires_num >= N:
        answer = cur_len # answer에는 cur_len의 가장 큰 값을 저장시킨다.
        cur_len += max_len
    # cur_len으로 N개의 랜선을 만들 수 없다면 cur_len에서 max_len // 2 를 뺀다.
    else:
        cur_len -= max_len

# cur_len을 1씩 증가시키면서 정답을 찾는다.
cur_len = answer + 1

while True:
    wires_num = 0
    index = bisect_left(wires, cur_len)

    if index < K:
        for wire in wires[index:]:
            wires_num += wire // cur_len

    # cur_len을 1씩 증가시키다가 더이상 랜선을 만들수 없는 경우 while문을 빠져나온다.
    if wires_num < N:
        break

    cur_len += 1

# cur_len으로 더이상 랜선을 만들수 없는 순간에 while문을 빠져 나왔으므로 정답은 cur_len - 1이다.
answer = cur_len - 1

print(answer)
