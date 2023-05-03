h, m, t = map(int, open(0).read().split())

total_m = h * 60 + m + t
print((total_m // 60) % 24, total_m % 60, sep=' ')