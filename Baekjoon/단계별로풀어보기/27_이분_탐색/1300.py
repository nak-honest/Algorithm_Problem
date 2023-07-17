# 여기에 이분탐색이 어떻게 쓰이는지 알아내는데 한시간정도 걸렸다.
# 알게되면 구현은 쉽다.

N = int(input())
k = int(input())


def get_kth_num(N, k):
    diff = N * N // 2
    cur_num = diff

    # cur_num이 계속 업데이트 되면서 해당 수가 k번째 수인지를 확인한다.
    while True:
        count = 0
        equal_count = 0

        # 각 행별로 cur_num보다 작거나 같은 수의 개수를 count에 더한다.
        # i 행에서 cur_num보다 작거나 같은 수의 개수는 cur_num // i 개이다.
        # 하지만 N*N 행렬이기 때문에 각 행에서 cur_num보다 작거나 같은 수는 N개보다 클 수 없다.
        for i in range(1, N+1):
            j = cur_num // i
            j = min(j, N)
            count += j

            # count는 cur_num보다 작거나 같은 개수를 저장한다.
            # 하지만 cur_num과 같은 수가 여러개 있을수 있기 때문에 cur_num과 같은 수가 있다면 equal_count에 따로 저장한다.
            if i*j == cur_num:
                equal_count += 1

        # count의 개수에 따라 cur_num에 diff//2 를 더하거나 뺀다. -> 여기서 이분탐색이 쓰인다.
        diff = max(diff//2, 1)

        # k가 count보다 크다면 k번째 수는 cur_num보다 큰 수이므로 diff를 더한다.
        if k > count:
            cur_num += diff
        # k가 count - equal_count 보다 작거나 같다면 k번째 수는 cur_num보다 작은 수 이므로 diff를 뺀다.
        elif k <= count - equal_count:
            cur_num -= diff
        # (count - equal_count) < k <= count 라면 k번째 수는 cur_num이거나 약간 작은 수 이다.
        # N*N 행렬에 정확히 cur_num이라는 수가 없을 수 있기 때문에 k번째 수는 cur_num보다 약간 작을 수 있는 것이다.
        else:
            break

    # cur_num이 N*N 행렬에 들어 있는지 확인한다. N*N 행렬에 들어 있다면 cur_num이 k번째 수이다.
    # 만약 들어있지 않다면 cur_num을 1 감소 시키고 해당 수가 들어있는지를 본다.
    while True:
        for i in range(1, N + 1):
            if cur_num // i <= N and cur_num % i == 0:
                return cur_num
        cur_num -= 1


print(get_kth_num(N, k))