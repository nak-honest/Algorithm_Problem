import sys
from collections import Counter

N, M = map(int, input().split())
words = [sys.stdin.readline().rstrip('\n') for _ in range(N)]
mem_words = Counter(filter(lambda s: len(s) >= M, words)).most_common()
voca_list = sorted(mem_words, key=lambda x: (-x[1], -len(x[0]), x[0]))

for voca in voca_list:
    print(voca[0])
