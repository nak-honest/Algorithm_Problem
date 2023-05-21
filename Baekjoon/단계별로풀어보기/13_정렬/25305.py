N, k, *scores = map(int, open(0).read().split())

print(sorted(scores, reverse=True)[k-1])