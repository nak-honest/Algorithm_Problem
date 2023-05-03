h, m = map(int, input().split())

total_m = h * 60 + m - 45
print((total_m // 60) % 24, total_m % 60, sep=' ')