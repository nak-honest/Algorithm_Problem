# 아직 DP에 익숙하지 않아서 밑의와 같은 풀이를 생각해내지 못했다.
# 내가 풀던 풀이는 첫번째로 싼 컬러와 두번째로 싼 컬러만 고려했고, 가장 비싼 컬러는 선택하지 않도록 풀었기 때문에
# 제대로 풀리지 않았다. DP에 대해 더 공부하고 문제도 많이 풀어야 한다.

import sys

N = int(input())
house_rgb = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
min_rgb = [[0, 0, 0] for _ in range(N)]
min_rgb[0] = house_rgb[0]


for i in range(1, N):
    min_rgb[i][0] = min(min_rgb[i-1][1], min_rgb[i-1][2]) + house_rgb[i][0]
    min_rgb[i][1] = min(min_rgb[i-1][0], min_rgb[i-1][2]) + house_rgb[i][1]
    min_rgb[i][2] = min(min_rgb[i-1][0], min_rgb[i-1][1]) + house_rgb[i][2]

print(min(min_rgb[-1]))