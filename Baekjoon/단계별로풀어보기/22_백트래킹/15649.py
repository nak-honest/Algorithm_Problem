N, M = map(int, input().split())
seq = [0 for _ in range(M)]


def get_seq(i):
    if promising(i):
        if i == M - 1:
            print(*seq)
        else:
            for n in range(1, N+1):
                seq[i+1] = n
                get_seq(i+1)


def promising(i):
    if i > 0 and seq[i] in seq[:i]:
        return False
    return True


get_seq(-1)