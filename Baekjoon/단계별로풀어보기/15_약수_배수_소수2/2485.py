from math import gcd
import sys

N = int(input())
loc = [int(sys.stdin.readline().rstrip('\n')) for _ in range(N)]
distance = [loc[i+1] - loc[i] for i in range(N-1)]

min_distance = gcd(*set(distance))
answer = sum(map(lambda d: (d // min_distance) - 1, distance))

print(answer)