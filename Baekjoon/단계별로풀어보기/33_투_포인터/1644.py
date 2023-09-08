import sys

N = int(input())

# 에라토스테네스의 체로 소수들을 빠르게 구한다.
def eratos(n):
    is_prime = [False] * 2 + [True] * (n-1)

    for i in range(2, n+1):
        if is_prime[i]:
            for j in range(2*i, n+1, i):
                is_prime[j] = False

    return list(filter(lambda x: is_prime[x], range(2, n+1)))

prime = eratos(N)

i = 0
j = 0

sub_sum = prime[i] if prime else 0

count = 0

# 투포인터로 연속된 합이 N이 되는 경우의 수를 센다.
while True:
    if sub_sum == N:
        count += 1
        j += 1
        if j >= len(prime):
            break

        sub_sum += prime[j]

    elif sub_sum > N and i + 1 <= j:
        sub_sum -= prime[i]
        i += 1

    else:
        j += 1
        if j >= len(prime):
            break

        sub_sum += prime[j]

print(count)
