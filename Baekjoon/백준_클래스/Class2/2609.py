def get_gcd(n, m):
    if n < m:
        n, m = m, n

    if m == 0:
        return n

    return get_gcd(m, n % m)


a, b = map(int, input().split())

gcd = get_gcd(a, b)
lcm = gcd * (a // gcd) * (b // gcd)

print(gcd, lcm, sep='\n')