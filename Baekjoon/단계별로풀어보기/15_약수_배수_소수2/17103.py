# 소수들을 미리 구하지 않아서 계속 시간 초과가 발생했다. 생각보다 많이 헤멨던 문제였다.
# 그래도 다른 사람의 풀이보다 좀 더 빠르게 동작한다.
import sys


# 아래의 eratos()는 에라토스테네스의 체를 이용한 함수로, 짝수는 미리 걸러 놓아서 조금 더 빠르게 동작한다.
def eratos(n):
    sqrt_n = int(n ** 0.5)
    nums = [i & 1 == 1 for i in range(n + 1)]
    nums[2] = True

    for i in range(3, sqrt_n + 1, 2):
        if nums[i]:
            for j in range(i << 1, n + 1, i):
                nums[j] = False

    return [2] + list(filter(lambda x: nums[x], range(3, n + 1, 2)))


# 매 케이스마다 소수를 구하면 시간 초과가 발생한다.
# 1,000,000 보다 작은 소수들을 미리 구해 놔야 시간 초과가 발생하지 않는다.
prime = dict.fromkeys(eratos(1000000), 0)

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline())
    count = 0
    for i in prime:
        if i > (N >> 1):
            break
        if (N - i) in prime:
            count += 1
    print(count)