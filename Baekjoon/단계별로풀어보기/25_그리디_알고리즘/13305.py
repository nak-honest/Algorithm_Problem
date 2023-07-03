# 매 구간마다 가장 낮은 주유소를 기준으로 왼쪽, 오른쪽 구간으로 나눈다.
# 그 후 가장 낮은 주유소에서 오른쪽 구간을 가는데 필요한 기름을 모두 산다.
# 왼쪽 구간에서는 다시 가장 낮은 주유소를 찾아서 왼쪽, 오른쪽 구간으로 나눈다.
# 이를 왼쪽 구간이 더이상 존재하지 않을때까지 반복한다.
# 근데 이렇게 그리디만 적용하면 시간초과가 발생했다.
# 따라서 dp도 함께 이용했다.

import sys

N = int(input())
road_len = list(map(int, sys.stdin.readline().split()))
gas_costs = list(map(int, sys.stdin.readline().split()))

# dp[i]에는 0 ~ i 도시중 가장 비용이 낮은 주유소의 가격과, 해당 주유소의 도시 index를 저장한다.
dp = [[gas_costs[0], 0]]

for i in range(1, N):
    if dp[i-1][0] > gas_costs[i]:
        dp.append([gas_costs[i], i])
    else:
        dp.append(dp[i-1])

min_cost = dp[-1][0]
min_index = dp[-1][1]
old_index = N - 1
total_costs = 0

while old_index > 0:
    # 오른쪽 구간을 지나기 위한 기름을 모두 산다.
    for i in range(min_index, old_index):
        total_costs += min_cost * road_len[i]

    old_index = min_index
    # 왼쪽 구간에서 가장 비용이 낮은 주유소를 찾는다.
    min_cost = dp[old_index - 1][0]
    min_index = dp[old_index - 1][1]

print(total_costs)