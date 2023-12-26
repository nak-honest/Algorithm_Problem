import sys
from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

chicken_houses = []
homes = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken_houses.append((i, j))
        elif city[i][j] == 1:
            homes.append((i, j))

home_to_chicken_dist = dict()

for home in homes:
    home_to_chicken_dist[home] = dict()
    for chicken_house in chicken_houses:
        home_to_chicken_dist[home][chicken_house] = abs(home[0] - chicken_house[0]) + abs(home[1] - chicken_house[1])

answer = sys.maxsize
for max_chicken_houses in combinations(chicken_houses, M):
    chicken_dist = 0
    for home in homes:
        min_dist = sys.maxsize

        for chicken_house in max_chicken_houses:
            min_dist = min(home_to_chicken_dist[home][chicken_house], min_dist)
        chicken_dist += min_dist
    answer = min(answer, chicken_dist)

print(answer)