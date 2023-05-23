import sys

N = int(input())
xy_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for xy in sorted(xy_list, key=lambda x: (x[1], x[0])):
    print(*xy)
