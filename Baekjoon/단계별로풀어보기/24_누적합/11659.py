# n이 1부터 시작하는 수열 시그마 공식대로 풀면 된다.
# i~j 까지의 시그마 합은 1~j 까지의 시그마 합에서 1~i 까지의 시그마 합을 뺸 것이다.

import sys

N, M = map(int, input().split())
num = list(map(int, sys.stdin.readline().split()))

sum_until = [0]
for i in range(N):
    sum_until.append(sum_until[-1] + num[i])

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(sum_until[j] - sum_until[i-1])