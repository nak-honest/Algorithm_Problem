import sys
from functools import reduce

for _ in range(int(input())):
    n = int(input())

    clothes = dict()

    for _ in range(n):
        name, kind = sys.stdin.readline().split()
        clothes[kind] = clothes.get(kind, 1) + 1

    if n:
        print(reduce(lambda x, y: x * y, clothes.values()) - 1)
    else:
        print(0)
