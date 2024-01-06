# 걸린 시간 : 20분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

import sys

N, M = map(int, input().split())
snd_line = input().split()

truth_know = set(map(int, snd_line[1:]))
need_truth = [False] * M

parties = []

for _ in range(M):
    party = list(map(int, sys.stdin.readline().split()))[1:]
    parties.append(set(party))

prev_need_count = -1
new_need_count = 0

while prev_need_count != new_need_count:
    prev_need_count = new_need_count
    for i in range(M):
        if not need_truth[i] and truth_know.intersection(parties[i]):
            need_truth[i] = True
            truth_know = truth_know.union(parties[i])

    new_need_count = need_truth.count(True)

print(need_truth.count(False))


