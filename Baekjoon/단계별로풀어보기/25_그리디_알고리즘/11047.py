import sys

N, K = map(int, input().split())

coins = [int(sys.stdin.readline()) for _ in range(N)]

count = 0
for coin in reversed(coins):
    if coin <= K:
        count += K // coin
        K = K % coin
    if K == 0:
        break

print(count)