# 에라토스테네스의 체 사용
def eratos_between_n_2n(n):
    nums = [True] * ((n << 1) + 1)
    nums[0], nums[1] = False, False

    for i in range(2, int((n << 1) ** 0.5) + 1):
        if nums[i]:
            for j in range(i << 1, (n << 1) + 1, i):
                nums[j] = False

    return len(list(filter(lambda i: nums[i], range(n + 1, (n << 1) + 1))))


cases = list(map(int, open(0).read().split()))
cases.pop()

for _n in cases:
    print(eratos_between_n_2n(_n))
