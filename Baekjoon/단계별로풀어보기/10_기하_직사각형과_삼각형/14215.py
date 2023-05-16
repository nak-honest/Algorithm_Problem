sides = list(map(int, input().split()))
# 가장 큰 변의 길이가 나머지 두변의 길이보다 작아야 한다. 즉 sum(sides) - max(sides) > max(sides) + 1 이어야 한다.
# 따라서 sum(sides) - 2*max(sides) -1 이 음수면 그만큼 최대 길이의 변을 줄여야 하고, 양수면 최대 길이의 변을 줄일 필요가 없다.
print(sum(sides) + min(sum(sides) - 2 * max(sides) - 1, 0))
