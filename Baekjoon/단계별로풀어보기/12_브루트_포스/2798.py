from itertools import combinations, takewhile

N, M, *cards = map(int, open(0).read().split())
three_card_sum = sorted(map(sum, combinations(cards, 3)))
lesser_than_M = list(takewhile(lambda s: s <= M, three_card_sum))

print(lesser_than_M[-1])
