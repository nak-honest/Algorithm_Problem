import sys

N, C = map(int, input().split())
X = sorted([int(sys.stdin.readline()) for _ in range(N)])

# diff 를 2씩 나누면서 cur_distance에 더하거 뺀다. 그리고 cur_distance 이상의 거리로 공유기를 놓을 수 있는지 체크한다.
diff = ((X[-1] - X[0]) // (C-1)) // 2

# cur_distance가 업데이트 될때마다 공유기 사이의 거리를 최소 cur_distance로 할수 있는지 체크한다.
cur_distance = diff
answer = 0

# 이분 탐색으로 먼저 정답에 가까운 최대 거리를 찾는다.
while diff >= 1:
    # count는 최소 cur_distance의 거리를 만족시켰을때의 공유기 개수를 저장한다.
    # X[0]에 먼저 공유기를 놓고 시작하기 때문에 count를 1로 설정한다.
    count = 1
    i = 0

    # cur_distance 이상의 거리가 되었을 때 공유기를 놓는다.
    for j in range(1, N):
        if X[j] - X[i] >= cur_distance:
            count += 1
            i = j

    # diff를 2로 나누어서 더하거나 뺸다. -> 이분탐색
    diff //= 2

    # cur_distance의 거리로 했을때 공유기의 개수가 C개를 넘는다면 cur_distance를 늘렸을때에도 공유기 개수가 C개 넘게 배치 할수 있는지 체크한다.
    # 따라서 cur_distance에 diff//2를 더한다.
    if count >= C:
        answer = cur_distance
        cur_distance += diff
    # cur_distance의 거리로 했을때 공유기의 개수가 C개보다 적다면 cur_distance를 줄여야 한다.
    # 따라서 diff//2를 뺀다.
    else:
        cur_distance -= diff

# 위의 이분 탐색을 통해 정답에 가까운 값을 찾았으면, 이제 거리를 1씩 증가시키면서 최대 거리를 찾는다.
while True:
    answer += 1
    count = 1
    i = 0

    for j in range(1, N):
        if X[j] - X[i] >= answer:
            count += 1
            i = j

    if count < C:
        answer -= 1
        break

print(answer)