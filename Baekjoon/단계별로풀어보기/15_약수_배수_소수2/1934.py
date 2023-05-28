import sys
from math import lcm

T = int(input())
cases = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
answer = [lcm(case[0], case[1]) for case in cases]
print(*answer, sep='\n')