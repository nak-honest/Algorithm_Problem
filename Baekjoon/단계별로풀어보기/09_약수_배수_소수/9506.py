cases = list(map(int, open(0).read().split()))
cases.pop()

for n in cases:
    divisor = list(filter(lambda i: n % i == 0, range(1, n)))
    if sum(divisor) == n:
        print(f'{n} = ', end='')
        print(*divisor, sep=' + ')
    else:
        print(f'{n} is NOT perfect.')
