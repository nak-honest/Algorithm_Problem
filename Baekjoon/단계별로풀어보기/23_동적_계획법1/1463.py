# DP 문제라고 소개되어 있는데 백트래킹으로 풀리긴 했다.
# 하지만 DP로도 풀어보자.

min_count = 1000000


def make_one(n, count):
    if promising(count):
        if n == 1:
            global min_count
            min_count = min(count, min_count)
        elif n % 3 != 0 and n % 2 != 0:
            make_one(n - 1, count + 1)
        elif n % 3 == 0 and n % 2 != 0:
            make_one(n // 3, count + 1)
            make_one(n - 1, count + 1)
        elif n % 3 != 0 and n % 2 == 0:
            make_one(n // 2, count + 1)
            make_one(n - 1, count + 1)
        else:
            make_one(n // 3, count + 1)
            make_one(n // 2, count + 1)


def promising(count):
    if count >= min_count:
        return False
    return True


N = int(input())

make_one(N, 0)
print(min_count)

