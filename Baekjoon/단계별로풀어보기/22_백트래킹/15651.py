N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
seq = [0 for _ in range(M)]


def get_seq(i):
    if i == M:
        print(*seq)
    else:
        for n in nums:
            seq[i] = n
            get_seq(i+1)


get_seq(0)