a1, a0, c, n0 = map(int, open(0).read().split())
print(int((a1 - c) <= 0 and (a1 - c) * n0 + a0 <= 0))
