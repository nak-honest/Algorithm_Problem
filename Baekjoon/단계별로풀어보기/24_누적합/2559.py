import sys

N, K = map(int, input().split())
num = list(map(int, sys.stdin.readline().split()))

temp_sum = sum(num[:K])
max_sum = temp_sum

for i in range(N-K):
    temp_sum -= num[i]
    temp_sum += num[i+K]

    max_sum = max(max_sum, temp_sum)

print(max_sum)